from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    data_inicio: Optional[datetime] = None
    data_fim: Optional[datetime] = None

class TarefaCreate(TarefaBase):
    pass


class TarefaResponse(TarefaBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    data_inicio: Optional[datetime] = None
    data_fim: Optional[datetime] = None
