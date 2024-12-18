from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, get_db
from backend.schemas import TarefaResponse, TarefaCreate, TarefaUpdate
from typing import List
from backend.crud import create_tarefa, select_all_tarefa, select_tarefa, delete_tarefa, update_tarefa


router = APIRouter()


@router.post("/tarefas/", response_model=TarefaResponse)
def post_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    """
    Rota de Criar um Tarefa no Banco de Dados
    """
    tarefa = create_tarefa(tarefa=tarefa,db=db)
    return tarefa

@router.get("/tarefas/", response_model=List[TarefaResponse])
def get_all_tarefas(db: Session = Depends(get_db)):
    tarefas = select_all_tarefa(db)
    return tarefas


@router.get("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def get_tarefa_with_id(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = select_tarefa(db=db,tarefa_id=tarefa_id)
    if not tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    return tarefa


@router.put("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def put_tarefa_with_id(tarefa_id: int, tarefa:TarefaUpdate, db: Session = Depends(get_db)):
    db_tarefa = select_tarefa(db=db,tarefa_id=tarefa_id)
    if not db_tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    tarefa = update_tarefa(db=db,tarefa_id=tarefa_id, tarefa=tarefa)
    return tarefa

@router.delete("/tarefas/{tarefa_id}")
def delete_tarefa_with_id(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = select_tarefa(db=db,tarefa_id=tarefa_id)
    if not tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    tarefa = delete_tarefa(db=db,tarefa_id=tarefa_id)
    return tarefa
