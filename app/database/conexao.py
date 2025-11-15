from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
porta = os.getenv("DB_PORT")
nome_db = os.getenv("DB_DATABASE")

engine = create_engine(f"mysql+mysqldb://{user}:{senha}@{host}:{porta}/{nome_db}")
#mysqldb é o nome interno do driver mysqlclient

Sessionlocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()