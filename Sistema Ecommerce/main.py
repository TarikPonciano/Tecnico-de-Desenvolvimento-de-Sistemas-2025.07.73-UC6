# Crie um menu contendo as opções Menu Cliente e Menu Produto

# Implemente as funcionalidades de CRUD para Cliente e Produto

from conexaoDB import ConexaoDB
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

meuBanco = ConexaoDB(dbname=DB_NAME, host=DB_HOST,
                     port=DB_PORT, user=DB_USER, password=DB_PASSWORD)


def menuCliente():
    while True:
        print("MENU CLIENTES")
        print('''
Operações:

1. Ver Clientes
2. Cadastrar Cliente
3. Atualizar Cliente
4. Remover Cliente

0. Voltar para o menu principal        
''')
        op = input("Digite o número da opção desejada:")

        if op == "1":
            verClientes()
        elif op == "2":
            cadastrarCliente()
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "0":
            print("Voltando para o menu principal...")
            break
        else:
            print("Escolha uma opção válida!")

        input("TECLE ENTER PARA CONTINUAR.")


def cadastrarCliente():
    print("CADASTRAR NOVO CLIENTE")

    nome = input("Digite o nome do novo cliente: ")

    resultado = meuBanco.manipular(
        "INSERT INTO cliente VALUES(default, %s);", (nome,))

    if resultado == "DEU CERTO!":
        print("Cliente cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar cliente!")


def verClientes():
    print("LISTA DE CLIENTES:")

    print("ID | Nome")

    clientes = meuBanco.consultar("SELECT * FROM cliente ORDER BY id_cliente;")

    if clientes == None:
        print("Erro ao consultar tabela Clientes!")
    elif len(clientes) == 0:
        print("NÃO HÁ CLIENTE CADASTRADOS")
    else:
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]}")


def menuProduto():
    while True:
        print("MENU PRODUTOS")
        print('''
Operações:

1. Ver Produtos
2. Cadastrar Produto
3. Atualizar Produto
4. Remover Produto

0. Voltar para o menu principal        
''')
        op = input("Digite o número da opção desejada:")

        if op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "0":
            print("Voltando para o menu principal...")
            break
        else:
            print("Escolha uma opção válida!")

        input("TECLE ENTER PARA CONTINUAR.")


while True:
    print("Boas vindas ao Ecommerce XYZ")

    print('''
Menu:

1. Menu Clientes
2. Menu Produtos
          
0. Sair
''')
    op = input("Digite o número da opção desejada:")

    if op == "1":
        menuCliente()
    elif op == "2":
        menuProduto()
    elif op == "0":
        print("Saindo do programa...")
        break
    else:
        print("Digite uma opção válida!")

    input("TECLE ENTER PARA CONTINUAR...")
