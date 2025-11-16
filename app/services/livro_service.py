import requests
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from ..repositories import livro_repository 
from .openlibrary_service import get_book_data 
from ..models.livro import Livro 

def cache_or_get_livro_by_olid(db: Session, olid: str) -> Optional[Livro]:
    db_livro = livro_repository.get_livro_por_olid(db, olid)
    
    if db_livro:
        return db_livro
    
    try:
        book_data = get_book_data(olid)
    except requests.exceptions.HTTPError as e:
        
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Livro com OLID {olid} não encontrado na OpenLibrary.")
        raise e
    if not book_data:
       
        raise HTTPException(status_code=500, detail=f"Falha desconhecida ao processar dados da OpenLibrary para {olid}.")

    db_livro = livro_repository.create_livro(db, book_data)
    
    return db_livro