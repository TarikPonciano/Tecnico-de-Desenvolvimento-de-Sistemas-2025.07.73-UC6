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
            atualizarCliente()
        elif op == "4":
            removerCliente()
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
        "INSERT INTO cliente VALUES(default, %s) RETURNING id_cliente;", (nome,))

    if resultado == "DEU CERTO!":
        print("Cliente cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar cliente!")


def verClientes():
    print("LISTA DE CLIENTES:")

    print("ID | Nome")

    clientes = meuBanco.consultar(
        "SELECT * FROM cliente ORDER BY id_cliente ASC;")

    if clientes == None:
        print("Erro ao consultar tabela Clientes!")
        return None
    elif len(clientes) == 0:
        print("NÃO HÁ CLIENTE CADASTRADOS")
        return None
    else:
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]}")
        return clientes


def atualizarCliente():
    # Visualizar Lista de Clientes
    # Escolher um cliente usando o id
    # Verificar que o cliente existe
    # Mostrar as informações atuais desse cliente
    # Pedir as novas informações (se vazio = manter anterior)
    # Executar manipulação no banco
    clientes = verClientes()

    if clientes == None:
        print("Não há clientes para modificar...")
        return

    idCliente = int(
        input("Digite o id do cliente a ser atualizado (0=cancelar): "))

    if idCliente <= 0:
        print("Você cancelou a operação!")
        return

    clienteEscolhido = None

    for cliente in clientes:
        if cliente[0] == idCliente:
            clienteEscolhido = cliente
            break

    if clienteEscolhido == None:
        print("Não foi encontrado um cliente com esse id!")
        return

    print(f'''
INFORMAÇÕES DO CLIENTE:
          
ID - {clienteEscolhido[0]}
NOME - {clienteEscolhido[1]}

''')
    print("Digite as novas informações a seguir. Deixe vazio para manter a informação original!")

    nome = input("Digite o novo nome:") or cliente[1]

    resultado = meuBanco.manipular('''
UPDATE cliente
SET
nome_cliente = %s
WHERE
id_cliente = %s;
''', (nome, clienteEscolhido[0]))

    if resultado == "DEU CERTO!":
        print("Cliente modificado com sucesso!")
    else:
        print("Erro ao modificar cliente!")


def removerCliente():
    clientes = verClientes()

    if clientes == None:
        print("Não há clientes para remover!")
        return

    idCliente = int(
        input("Digite o id do cliente que deseja remover (0=cancelar): "))

    if idCliente <= 0:
        print("Operação cancelada!")
        return
    else:
        clienteEscolhido = None

        for cliente in clientes:
            if cliente[0] == idCliente:
                clienteEscolhido = cliente
                break

        if clienteEscolhido == None:
            print("ID de Cliente não encontrado!")
        else:
            print(f'''
INFORMAÇÕES DO CLIENTE:

ID: {clienteEscolhido[0]}
NOME: {clienteEscolhido[1]}

''')
            resultado = meuBanco.manipular(
                "DELETE FROM cliente WHERE id_cliente = %s;", (clienteEscolhido[0],))

            if resultado == "DEU CERTO!":
                print(f"Cliente {clienteEscolhido[0]} Removido com Sucesso")
            else:
                print(f"Falha ao remover o Cliente {clienteEscolhido[0]}")


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
            verProdutos()
        elif op == "2":
            cadastrarProduto()
        elif op == "3":
            atualizarProduto()
        elif op == "4":
            removerProduto()
        elif op == "0":
            print("Voltando para o menu principal...")
            break
        else:
            print("Escolha uma opção válida!")

        input("TECLE ENTER PARA CONTINUAR.")


def verProdutos():
    print("LISTA DE PRODUTOS:")

    print("ID | Nome | R$ Preço | Estoque")

    produtos = meuBanco.consultar(
        "SELECT * FROM produto ORDER BY id_produto ASC;")

    if produtos == None:
        print("Erro ao consultar tabela Produtos!")
        return None
    elif len(produtos) == 0:
        print("NÃO HÁ PRODUTO CADASTRADOS")
        return None
    else:
        for produto in produtos:
            print(
                f"{produto[0]} | {produto[1]} | R$ {produto[2]} | {produto[3]}")
        return produtos


def cadastrarProduto():
    print("CADASTRAR NOVO PRODUTO")

    nome = input("Digite o nome do produto:")
    preco = float(input("Digite o preço do produto:"))
    estoque = int(input("Digite o estoque do produto: "))

    resultado = meuBanco.manipular(
        "INSERT INTO produto VALUES (default, %s, %s, %s);", (nome, preco, estoque))

    if resultado == "DEU CERTO!":
        print("Produto cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar produto!")


def atualizarProduto():
    produtos = verProdutos()

    if produtos == None:
        print("Não há produtos para modificar...")
        return

    idProduto = int(
        input("Digite o id do produto que deseja modificar (0 = cancelar): "))

    if idProduto <= 0:
        print("Operação Cancelada...")
        return

    produtoEscolhido = None

    for produto in produtos:
        if produto[0] == idProduto:
            produtoEscolhido = produto
            break

    if produtoEscolhido == None:
        print("Produto não foi encontrado...")
        return

    print(f'''
INFORMAÇÕES DO PRODUTO:

ID - {produtoEscolhido[0]}
Nome - {produtoEscolhido[1]}
Preço - R$ {produtoEscolhido[2]}
Estoque - {produtoEscolhido[3]}

''')
    print("Preencha as informações a seguir. Vazio para manter o original.")
    nome = input("Digite o novo nome do produto:") or produtoEscolhido[1]
    preco = float(input("Digite o novo preço do produto:")
                  or produtoEscolhido[2])
    estoque = int(input("Digite o novo estoque do produto:")
                  or produtoEscolhido[3])

    resultado = meuBanco.manipular('''
UPDATE produto
SET
nome_produto = %s,
preco_produto = %s,
estoque_produto = %s
WHERE id_produto = %s;''', (nome, preco, estoque, produtoEscolhido[0]))

    if resultado == "DEU CERTO!":
        print("Produto modificado com sucesso.")
    else:
        print("Não foi possível modificar o produto.")


def removerProduto():
    produtos = verProdutos()

    if produtos == None:
        print("Não há produtos para modificar...")
        return

    idProduto = int(
        input("Digite o id do produto que deseja modificar (0 = cancelar): "))

    if idProduto <= 0:
        print("Operação Cancelada...")
        return

    produtoEscolhido = None

    for produto in produtos:
        if produto[0] == idProduto:
            produtoEscolhido = produto
            break

    if produtoEscolhido == None:
        print("Produto não foi encontrado...")
        return

    print(f'''
INFORMAÇÕES DO PRODUTO:

ID - {produtoEscolhido[0]}
Nome - {produtoEscolhido[1]}
Preço - R$ {produtoEscolhido[2]}
Estoque - {produtoEscolhido[3]}

''')
    resultado = meuBanco.manipular('''
DELETE FROM produto
WHERE id_produto = %s;
''', (produtoEscolhido[0],))

    if resultado == "DEU CERTO!":
        print("Produto removido com sucesso!")
    else:
        print("Erro ao remover produto!")


while True:
    print("Boas vindas ao Ecommerce XYZ")

    print('''
Menu:

1. Menu Clientes
2. Menu Produtos
3. Comprar
          
0. Sair
''')
    op = input("Digite o número da opção desejada:")

    if op == "1":
        menuCliente()
    elif op == "2":
        menuProduto()
    elif op == "3":
        realizarCompra()
    elif op == "0":
        print("Saindo do programa...")
        break
    else:
        print("Digite uma opção válida!")

    input("TECLE ENTER PARA CONTINUAR...")
