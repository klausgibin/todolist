# Projeto de TO DO List

## Visão Geral

Este projeto é uma aplicação de gerenciamento de tarefas bem simples que utiliza **FastAPI** para o backend, **Streamlit** para o frontend, e **SQLAlchemy** com **SQLite** para persistência de dados. A validação de dados é realizada com **Pydantic**.

## Estrutura do Projeto

<pre>
todolist/
<span style="font-size: 16px;">📁</span> backend/
   <span style="font-size: 16px;">📄</span> models.py
   <span style="font-size: 16px;">📄</span> schemas.py
   <span style="font-size: 16px;">📄</span> database.py
   <span style="font-size: 16px;">📄</span> crud.py
   <span style="font-size: 16px;">📄</span> router.py
   <span style="font-size: 16px;">📄</span> main.py
<span style="font-size: 16px;">📁</span> frontend/
   <span style="font-size: 16px;">📄</span> api_client.py
   <span style="font-size: 16px;">📄</span> app.py
   <span style="font-size: 16px;">📄</span> button_functions.py
   <span style="font-size: 16px;">📄</span> ui_components.py
<span style="font-size: 16px;">🗄️</span> database.db
</pre>

### Backend

- <span style="font-size: 16px;">📄</span> **models.py**: Define os modelos SQLAlchemy para as tabelas do banco de dados.
- <span style="font-size: 16px;">📄</span> **schemas.py**: Contém os esquemas Pydantic para validação de dados.
- <span style="font-size: 16px;">📄</span> **database.py**: Configuração da conexão com o banco de dados SQLite.
- <span style="font-size: 16px;">📄</span> **crud.py**: Funções para operações CRUD (Create, Read, Update, Delete).
- <span style="font-size: 16px;">📄</span> **router.py**: Define as rotas da API FastAPI.
- <span style="font-size: 16px;">📄</span> **main.py**: Ponto de entrada da aplicação FastAPI.

### Frontend

- <span style="font-size: 16px;">📄</span> **api_client.py**: Cliente para comunicação com a API backend.
- <span style="font-size: 16px;">📄</span> **app.py**: Aplicação principal Streamlit.
- <span style="font-size: 16px;">📄</span> **button_functions.py**: Funções associadas aos botões da interface.
- <span style="font-size: 16px;">📄</span> **ui_components.py**: Componentes reutilizáveis da interface do usuário.

### Banco de Dados

- <span style="font-size: 16px;">🗄️</span> **database.db**: Arquivo do banco de dados SQLite local.

## Pré-requisitos

- Python 3.12.* (pode ser instalado via pyenv)
- Poetry

## Instalação e Execução

_Nota: Os seguintes comandos são para ambiente Windows usando o terminal Git Bash._

1. **Instale as dependências:**
   ```bash
   poetry install
   source .venv/scripts/activate
   uvicorn backend.main:app --reload & streamlit run ./frontend/app.py &


### Tecnologias Utilizadas


<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="200"/>

**FastAPI:** Framework web rápido para construção de APIs com Python.
<br><br>


<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" alt="Streamlit" width="200"/>

**Streamlit:** Biblioteca para criação de aplicações web de dados.
<br><br>


<img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="SQLAlchemy" width="200"/>

**SQLAlchemy:** Toolkit SQL e ORM para Python.
<br><br>


<img src="https://www.sequoiacap.com/wp-content/uploads/sites/6/2023/08/name-and-logo-path.svg" alt="Pydantic" width="200"/>

**Pydantic:** Biblioteca para validação de dados e gerenciamento de configurações.
<br><br>


 <img src="https://w7.pngwing.com/pngs/71/296/png-transparent-sqlite-hd-logo-thumbnail.png" alt="SQLLite" width="200"/>

**SQLite:** Sistema de gerenciamento de banco de dados relacional leve.
<br><br>

_Este README fornece uma visão geral básica do projeto. Para informações mais detalhadas sobre cada componente, consulte os comentários nos respectivos arquivos de código._