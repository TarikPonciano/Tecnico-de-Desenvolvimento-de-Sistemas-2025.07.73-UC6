from database import Base, engine, Session
from models import Livro, Cliente, Aluguel
from datetime import date


def configurarBanco():
    Base.metadata.drop_all(bind=engine)
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


def cadastrarCliente():

    print("Cadastro de Novo Cliente")

    nome = input("Digite o nome do cliente:")
    email = input("Digite o email do cliente:")

    cliente = Cliente(nome=nome, email=email)

    session = Session()
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    session.close()

    print(cliente)


def verClientes():

    print("Lista de Clientes:")

    session = Session()
    clientes = session.query(Cliente).all()
    session.close()

    print("ID | Nome | Email")
    for cliente in clientes:
        print(f"{cliente.id} | {cliente.nome} | {cliente.email}")


def cadastrarAluguel():

    verClientes()

    idCliente = int(
        input("Digite o id do cliente que está realizando o aluguel: "))

    verLivros()

    idLivro = int(input("Digite o id do livro que está sendo alugado: "))

    aluguel = Aluguel(cliente_id=idCliente, livro_id=idLivro)

    session = Session()
    session.add(aluguel)
    session.commit()
    session.refresh(aluguel)
    print("Aluguel Criado com Sucesso")
    aluguel.mostrarInformacoes()
    session.close()


def verAlugueis():
    print("Lista de Alugueis: ")

    print("ID | Nome do Cliente | Titulo do Livro")

    session = Session()
    alugueis = session.query(Aluguel).all()
    session.close()

    for aluguel in alugueis:
        print(f"{aluguel.id} | {aluguel.cliente.nome} | {aluguel.livro.titulo} ")


while True:

    print("Menu: ")
    print('''
1. Cadastrar Livro
2. Ver Livros
          
3. Cadastrar Cliente
4. Ver Clientes
          
5. Cadastrar Aluguel
6. Ver Alugueis

9. Configurar Banco de Dados
0. Sair
''')
    op = input("Digite a opção desejada do menu:")

    if op == "1":
        cadastrarLivro()
    elif op == "2":
        verLivros()
    elif op == "3":
        cadastrarCliente()
    elif op == "4":
        verClientes()
    elif op == "5":
        cadastrarAluguel()
    elif op == "6":
        verAlugueis()
    elif op == "9":
        configurarBanco()
    elif op == "0":
        print("Saindo do Programa...")
        break
    else:
        print("Opção inválida!")

    input("TECLE ENTER PARA CONTINUAR.")
