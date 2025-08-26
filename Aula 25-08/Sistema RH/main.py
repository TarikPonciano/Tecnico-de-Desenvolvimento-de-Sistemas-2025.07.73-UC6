# Crie um menu dentro de um laço while, com as opções:
# 1. Criar Funcionário
# 2. Ver Funcionário
# A funcionalidade Criar Funcionário pede as informações básicas nome, cpf, salário, cargo e departamento e registra o novo funcionário no banco
# A funcionalidade Ver Funcionário exibe todos os funcionarios cadastrados em lista.

import psycopg2
import dotenv
import os


def verFuncionarios():
    print("LISTA DE FUNCIONÁRIOS")

    print("ID | Nome | CPF | Salário R$ | Cargo | Departamento")

    try:
        conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST,
                                port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM funcionario
        ORDER BY id_funcionario ASC;
''')
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)
        resultado = None

    if resultado == None:
        print("Falha ao carregar os arquivos")
    else:
        for func in resultado:
            print(
                f"{func[0]} | {func[1]} | {func[2]} | R$ {func[3]:.2f }| {func[4]} | {func[5]}")


dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

print("Sistema RH")

while True:
    print("Escolha uma das opções a seguir:")

    print('''
    1. Ver Funcionários
    2. Cadastrar Funcionário
    0. Sair
''')

    op = input("Digite a opção desejada:")

    if op == "1":
        verFuncionarios()
    elif op == "2":
        pass
    elif op == "0":
        print("Saindo do Programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    input("TECLE ENTER PARA CONTINUAR.")
