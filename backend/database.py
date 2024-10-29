from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#@contextmanager
def get_db() -> Session:
    with SessionLocal() as session:
        yield session