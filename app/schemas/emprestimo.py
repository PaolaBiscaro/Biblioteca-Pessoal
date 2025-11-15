from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmprestimoBase(BaseModel):
    status: bool
    data: date
    borrower_name: Optional[str]


class EmprestimoRequest(BaseModel):
    livro_id: int


class EmpestimoResponse(EmprestimoBase):
    id_emprestimo: int
    livro_id: int
    
    class Config:
        from_attributes = True
        populate_by_name = True