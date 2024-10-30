import streamlit as st
import pandas as pd
from api_client import update_task, create_task, delete_task, fetch_data

def handle_save_changes(edited_df, original_df):
    changes_made = False
    rows_to_delete = []

    for index, row in edited_df.iterrows():
        if 'delete' in row and row['delete']:
            rows_to_delete.append(row['id'])
            continue

        if index >= len(original_df):  # Nova linha
            changes_made = handle_new_task(row) or changes_made
        elif not row.equals(original_df.loc[index]):  # Linha existente modificada
            changes_made = handle_updated_task(row) or changes_made

    # Excluindo tarefas marcadas para exclusão
    for task_id in rows_to_delete:
        changes_made = handle_delete_task(task_id) or changes_made

    if changes_made:
        st.session_state.data = fetch_data()
        st.rerun()
    else:
        st.info("Sem alterações para salvar.")

def handle_new_task(row):
    new_task = prepare_task_data(row)
    try:
        response = create_task(new_task)
        st.success(f"Nova tarefa criada: {response}")
        return True
    except Exception as e:
        st.error(f"Erro ao criar nova tarefa: {str(e)}")
        return False

def handle_updated_task(row):
    task_id = row['id']
    updated_data = prepare_task_data(row)
    try:
        response = update_task(task_id, updated_data)
        st.success(f"Tarefa {task_id} atualizada: {response}")
        return True
    except Exception as e:
        st.error(f"Erro ao atualizar tarefa {task_id}: {str(e)}")
        return False

def handle_delete_task(task_id):
    try:
        response = delete_task(task_id)
        st.success(f"Tarefa {task_id} excluída: {response}")
        return True
    except Exception as e:
        st.error(f"Erro ao excluir tarefa {task_id}: {str(e)}")
        return False

def prepare_task_data(row):
    task_data = row.to_dict()
    task_data.pop('id', None)
    task_data.pop('criado_em', None)
    task_data.pop('delete', None)
    
    for date_field in ['data_inicio', 'data_fim']:
        if pd.isnull(task_data[date_field]):
            task_data[date_field] = None
        else:
            task_data[date_field] = task_data[date_field].strftime('%Y-%m-%d')
    
    return task_data