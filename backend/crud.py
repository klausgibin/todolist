from sqlalchemy.orm import Session
from models import TarefaModel
from schemas import TarefaCreate, TarefaUpdate


def create_tarefa(db: Session, tarefa: TarefaCreate):
    db_tarefa = TarefaModel(**tarefa.model_dump())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa


def select_all_tarefa(db: Session,skip: int = 0, limit: int = 100):
    db_tarefa = db.scalars(select(TarefaModel).offset(skip).limit(limit)).all()
    return {db_tarefa}


def select_tarefa(db: Session, tarefa_id: int):
    db_tarefa = db.scalar(select(TarefaModel).filter_by(id=tarefa_id))
    return db_tarefa


def delete_tarefa(db: Session, tarefa_id: int):
    db_tarefa = db.scalar(select(TarefaModel).filter_by(id=tarefa_id))
    if not db_tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    db.delete(db_tarefa)
    db.commit()
    return {'message': 'Tarefa Deletada'}

# update com ID
def update_tarefa(db: Session, tarefa_id: int, tarefa: TarefaUpdate):
    db_tarefa = db.scalar(select(TarefaModel).filter_by(id=tarefa_id))
    if not db_tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    
    if tarefa.titulo is not None:
        db_tarefa.titulo = tarefa.titulo

    if tarefa.descricao is not None:
        db_tarefa.descricao = tarefa.descricao

    if tarefa.data_inicio is not None:
        db_tarefa.data_inicio = tarefa.data_inicio

    if tarefa.data_fim is not None:
        db_tarefa.data_fim = tarefa.data_fim

    db.update(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

