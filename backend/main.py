from fastapi import FastAPI
from database import engine
import models
from router import router

# Criando Tabelas Caso não Existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)