from sqlalchemy import Column,Integer, String, Date,DateTime
from sqlalchemy.sql import func
from backend.database import Base

class TarefaModel(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    criado_em = Column(DateTime, default=func.now())




