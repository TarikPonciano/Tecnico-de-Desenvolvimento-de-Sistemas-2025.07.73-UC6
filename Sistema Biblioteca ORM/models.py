from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Livro(Base):
    __tablename__ = "livro"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False, default="Autor Não Identificado")
    ano_publicacao = Column(Integer, nullable=False)

    alugueis = relationship("Aluguel", back_populates='livro')

    def mostrarInformacoes(self):
        print(f'''
Informações do Livro:

ID - {self.id}
Titulo - {self.titulo}
Autor - {self.autor}
Ano Publicação - {self.ano_publicacao}
''')

    def __repr__(self):
        return f"<Livro {self.titulo}>"


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)

    alugueis = relationship("Aluguel", back_populates="cliente", lazy="joined")
    
    def mostrarInformacoes(self):

        print(f'''
Informações do Cliente:
              
ID - {self.id}
Nome - {self.nome}
Email - {self.email}

''')

    def __repr__(self):
        return f"<Cliente {self.nome}>"


class Aluguel(Base):
    __tablename__ = "aluguel"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    livro_id = Column(Integer, ForeignKey("livro.id"), nullable=False)

    livro = relationship("Livro", back_populates="alugueis", lazy="joined")
    cliente = relationship("Cliente", back_populates="alugueis", lazy="joined")

    def __repr__(self):
        return f"<Aluguel {self.livro.titulo} - {self.cliente.nome}>"

    def mostrarInformacoes(self):
        print(f'''
Informações do Aluguel:
              
ID - {self.id}
Titulo do Livro - {self.livro.titulo}
Cliente - {self.cliente.nome}
''')
