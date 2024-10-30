import streamlit as st
from api_client import fetch_data
from ui_components import setup_page, get_column_config, prepare_dataframe, create_data_editor
from button_functions import handle_save_changes

def main():
    st.set_page_config(layout="wide")
    st.title("FastAPI + Streamlit - Cadastro de Tarefas")

    if 'data' not in st.session_state:
        st.session_state.data = fetch_data()

    df = prepare_dataframe(st.session_state.data)

    edited_df = create_data_editor(df, get_column_config())

    if st.button("Salvar Alterações"):
        handle_save_changes(edited_df, df)

if __name__ == "__main__":
    main()