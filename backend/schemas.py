from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from pydantic import validator

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

    @validator('data_inicio', 'data_fim', pre=True)
    def validate_date(cls, data):
        if data == "":
            return None
        if data is None:
            return None
        if isinstance(data, str):
            return date.fromisoformat(data)
        return data

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
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
