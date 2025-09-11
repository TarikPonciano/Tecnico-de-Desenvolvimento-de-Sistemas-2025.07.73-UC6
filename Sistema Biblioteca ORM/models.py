from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Livro(Base):
    __tablename__ = "livro"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False, default="Autor Não Identificado")
    ano_publicacao = Column(Integer, nullable=False)

    def __repr__(self):
        return f'''
Informações do Livro:

ID - {self.id}
Titulo - {self.titulo}
Autor - {self.autor}
Ano Publicação - {self.ano_publicacao}
'''
