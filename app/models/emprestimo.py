from ..database.conexao import Base
from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
    
class Emprestimo(Base):
    __tablename__ = "emprestimos"
    
    id = Column("id_emprestimo", Integer, primary_key=True, autoincrement=True)
    status = Column("status", Boolean,nullable=False)
    data = Column("data", Date,nullable=False)
    livro_id = Column("livro_id", ForeignKey("livros.id_livro"),nullable=False)

    def __init__(self, status, data, livro_id):
        self.status = status
        self.data = data
        self.livro_id = livro_id