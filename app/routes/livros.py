from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from ..database import get_db
from ..services.livro_service import cache_or_get_livro_by_olid
from ..schemas import LivroSchema  # seu Pydantic schema

router = APIRouter(prefix="/livros", tags=["Livros"])

@router.get("/{olid}", response_model=LivroSchema)
def buscar_livro(olid: str, db: Session = Depends(get_db)):
    livro = cache_or_get_livro_by_olid(db, olid)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro


@router.get("/", response_model=list[LivroSchema])
def listar_livros(db: Session = Depends(get_db)):
    from ..repositories import livro_repository
    return livro_repository.get_all_livros(db)


@router.put("/{olid}/status", response_model=LivroSchema)
def atualizar_status(olid: str, status: str, db: Session = Depends(get_db)):
    from ..repositories import livro_repository
    livro = livro_repository.get_livro_por_olid(db, olid)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    livro.status = status
    db.commit()
    db.refresh(livro)
    return livro




