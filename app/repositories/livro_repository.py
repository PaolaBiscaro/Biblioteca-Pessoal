from sqlalchemy.orm import Session
from ..models.livro import Livro


def get_livro_por_olid(db: Session, olid: str):
    return db.query(Livro).filter(Livro.olid == olid).first()


def create_livro(db: Session, book_data: dict):
    db_livro = Livro(
        olid=book_data["olid"],
        titulo=book_data["titulo"],
        autor=book_data["autor"]
    )
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro