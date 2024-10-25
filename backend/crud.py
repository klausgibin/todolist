from sqlalchemy.orm import Session
from models import TarefaModel
from schemas import TarefaCreate, TarefaUpdate


def criar_tarefa(db: Session, tarefa: TarefaCreate):
    db_tarefa = TarefaModel(**tarefa.model_dump())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa


def obter_todas_tarefa(db: Session,skip: int = 0, limit: int = 100):
    db_tarefa = db.scalars(select(TarefaModel).offset(skip).limit(limit)).all()
    return {'tarefas': db_tarefa}


def obter_tarefa(db: Session, tarefa_id: int):
    db_tarefa = db.execute(select(TarefaModel).filter_by(id=tarefa_id))
    if not db_tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    return db_tarefa


def deletar_tarefa(db: Session, tarefa_id: int):
    db_tarefa = db.execute(select(TarefaModel).filter_by(id=tarefa_id))
    if not db_tarefa:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Tarefa Não Encontrada'
        )
    db.delete(db_tarefa)
    db.commit()
    return {'message': 'Tarefa Deletada'}

# update com ID
def atualizar_tarefa(db: Session, tarefa: TarefaUpdate):
    pass














def obter_tarefa(db: Session, tarefa_id: int):
    return db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()