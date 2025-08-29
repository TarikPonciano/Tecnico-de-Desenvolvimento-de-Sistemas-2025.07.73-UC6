# Criar as funcionalidades:
# 1 - Atualizar Funcionário - Modificando as informações cadastradas de um funcionário
# 2 - Remover Funcionário - Apaga o funcionário do banco
# 3 - Atualizar Departamento
# 4 - Remover Departamento
# Bônus: Ao ver lista de funcionários, permitir escolher 1 funcionário e ver detalhes.
# Bônus 2: Ao ver lista de funcionários, exibir o nome do departamento no lugar do id do departamento


import dotenv
import os
from conexaoDB import ConexaoDB

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

meuBanco = ConexaoDB(dbname=DB_NAME, host=DB_HOST,
                     port=DB_PORT, user=DB_USER, password=DB_PASSWORD)


def verFuncionarios():
    print("LISTA DE FUNCIONARIOS")

    funcionarios = meuBanco.consultar(
        '''SELECT * FROM funcionario ORDER BY id_funcionario ASC;''', [])

    print("ID | NOME | CPF | SALÁRIO | CARGO | DEPARTAMENTO")
    for func in funcionarios:
        print(
            f"{func[0]} | {func[1]} | {func[2]} | R$ {func[3]} | {func[4]} | {func[5]}")


def cadastrarFuncionario():
    print("CADASTRO DE FUNCIONÁRIO")

    nome = input("Digite o nome do novo funcionário:")
    cpf = input("Digite o cpf do novo funcionário:")
    salario = float(input("Digite o salario do novo funcionário:"))
    cargo = input("Digite o cargo do novo funcionário:")

    verDepartamentos()
    departamento = int(
        input("Digite o id do departamento do novo funcionário (0 = sem departamento):"))

    if departamento == 0:
        departamento = None

    resultado = meuBanco.manipular('''
INSERT INTO funcionario
VALUES (default, %s, %s, %s, %s, %s);
''', (nome, cpf, salario, cargo, departamento))

    if resultado == "DEU CERTO!":
        print("Funcionário Cadastrado com Sucesso!")
    else:
        print("Erro ao Cadastrar Funcionário")


def cadastrarDepartamento():
    print("CADASTRO DE DEPARTAMENTO")
    nome = input("Digite o nome do departamento: ")

    resultado = meuBanco.manipular('''
INSERT INTO departamento
VALUES(default, %s);
''', (nome,))

    if resultado == "DEU CERTO!":
        print("Departamento cadastrado com sucesso!")


def verDepartamentos():
    print("LISTA DE DEPARTAMENTOS")

    departamentos = meuBanco.consultar(
        "SELECT * FROM departamento ORDER BY id_departamento ASC;", [])

    print("ID | NOME")

    for dep in departamentos:
        print(f"{dep[0]} | {dep[1]}")


def menuFuncionarios():

    while True:
        print("MENU FUNCIONARIOS")
        print('''Escolha uma opção abaixo:
1. Ver Funcionários
2. Cadastrar Funcionário
0. Voltar para menu principal''')
        op = input("Digite o número da opção desejada: ")

        if op == "1":
            verFuncionarios()
        elif op == "2":
            cadastrarFuncionario()
        elif op == "0":
            print("Voltando para o menu principal...")
            break
        else:
            print("Escolha uma opção válida!")

        input("TECLE ENTER PARA CONTINUAR...")


def menuDepartamentos():

    while True:
        print("MENU DEPARTAMENTOS")
        print('''Escolha uma opção abaixo:
1. Ver Departamentos
2. Cadastrar Departamento
0. Voltar para menu principal''')
        op = input("Digite o número da opção desejada: ")

        if op == "1":
            verDepartamentos()
        elif op == "2":
            cadastrarDepartamento()
        elif op == "0":
            print("Voltando para o menu principal...")
            break
        else:
            print("Escolha uma opção válida!")

        input("TECLE ENTER PARA CONTINUAR...")


print("BEM VINDO AO SISTEMA RH")
while True:
    print('''
Escolha uma opção do menu:

1. Menu Funcionários
2. Menu Departamentos
0. Sair
''')
    op = input("Digite o número da opção desejada:")

    if op == "1":
        menuFuncionarios()
    elif op == "2":
        menuDepartamentos()
    elif op == "0":
        print("Saindo do programa...")
        break

    input("TECLE ENTER PARA CONTINUAR")
