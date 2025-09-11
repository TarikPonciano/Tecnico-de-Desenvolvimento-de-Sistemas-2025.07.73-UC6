from database import Base, engine, Session
from models import Livro
from datetime import date


def configurarBanco():
    Base.metadata.create_all(bind=engine)


def cadastrarLivro():
    print("Cadastro de Novo Livro")

    novoTitulo = input("Digite o titulo do livro: ")
    novoAutor = input("Digite o autor do livro: ")
    novoAno_publicacao = int(input("Digite o ano de publicação do livro: "))

    novoLivro = Livro(titulo=novoTitulo, autor=novoAutor,
                      ano_publicacao=novoAno_publicacao)

    session = Session()
    session.add(novoLivro)
    session.commit()
    session.refresh(novoLivro)
    session.close()
    print("Livro Cadastrado:", novoLivro)

def verLivros():

    print("Lista de Livros: ")

    session = Session()
    livros = session.query(Livro).all()
    session.close()

    print("ID | Titulo | Autor | Ano")
    for livro in livros:
        print(f"{livro.id} | {livro.titulo} | {livro.autor} | {livro.ano_publicacao}")


while True:

    print("Menu: ")
    print('''
1. Cadastrar Livro
2. Ver Livros

9. Configurar Banco de Dados
0. Sair
''')
    op = input("Digite a opção desejada do menu:")

    if op == "1":
        cadastrarLivro()
    elif op == "2":
        verLivros()
    elif op == "9":
        configurarBanco()
    elif op == "0":
        print("Saindo do Programa...")
        break
    else:
        print("Opção inválida!")

    input("TECLE ENTER PARA CONTINUAR.")
