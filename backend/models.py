from sqlalchemy import Column,Interger, String, DataTime
from sqlalchemy.sql import func
from database import Base

class TarefaModel(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_inicio = Column(DateTime, nullable=True)
    data_fim = Column(DateTime, nullable=True)
    criado_em = Column(DateTime, default=func.now())




