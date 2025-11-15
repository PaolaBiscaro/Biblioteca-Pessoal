from ..database.conexao import Base
from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey

class Livro(Base):
    __tablename__ = "livros"
    
    id = Column("id_livro", Integer,primary_key=True, autoincrement=True)
    titulo = Column("titulo", String, nullable=False)
    autor = Column("autor", String, nullable=False)
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
