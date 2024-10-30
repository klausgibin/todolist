import streamlit as st
import pandas as pd


def get_column_config():
    return {
        "id": st.column_config.NumberColumn(
            "ID", help="Task ID", disabled=True, width="small",
        ),
        "titulo": st.column_config.TextColumn(
            "Título", help="Título da tarefa", width="medium",
        ),
        "descricao": st.column_config.TextColumn(
            "Descrição", help="Descrição da tarefa", width="large",
        ),
        "data_inicio": st.column_config.DateColumn(
            "Data de Início", help="Data de início da tarefa", width="medium",
        ),
        "data_fim": st.column_config.DateColumn(
            "Data de Fim", help="Data de fim da tarefa", width="medium",
        ),
        "criado_em": st.column_config.DatetimeColumn(
            "Criado em", help="Data e hora de criação", disabled=True, width="medium",
        ),
        "delete": st.column_config.CheckboxColumn(
            "Excluir", help="Marque para excluir a tarefa", default=False, width="small",
        ),
    }

def prepare_dataframe(data):
    df = pd.DataFrame(data)
    df['data_inicio'] = pd.to_datetime(df['data_inicio'])
    df['data_fim'] = pd.to_datetime(df['data_fim'])
    df['criado_em'] = pd.to_datetime(df['criado_em'])
    df['delete'] = False
    return df

def create_data_editor(df, column_config):
    return st.data_editor(
        df,
        column_config=column_config,
        num_rows="dynamic",
        use_container_width=True,
    )