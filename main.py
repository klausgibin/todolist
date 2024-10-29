from fastapi import FastAPI
from backend.database import engine
from backend import models
from backend.router import router
import uvicorn

app = FastAPI()
# Criando Tabelas Caso não Existam
models.Base.metadata.create_all(bind=engine)
app.include_router(router)

if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

