from pydantic import BaseModel

class LivroBase(BaseModel):
    titulo: str
    autor: str
    
    
class LivroRequest(BaseModel):
    olid: str 


class LivroResponse(LivroBase):
    id_livro: int 
    olid: str 
    
    class Config:
        from_attributes = True
        populate_by_name = True