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

    funcionarios = meuBanco.consultar('''SELECT * FROM funcionario''', [])

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


print("BEM VINDO AO SISTEMA RH")
while True:
    print('''
Escolha uma opção do menu:

1. Ver Funcionários
2. Cadastrar Funcionário
0. Sair
''')
    op = input("Digite o número da opção desejada:")

    if op == "1":
        verFuncionarios()
    elif op == "2":
        cadastrarFuncionario()
    elif op == "0":
        print("Saindo do programa...")
        break

    input("TECLE ENTER PARA CONTINUAR")
