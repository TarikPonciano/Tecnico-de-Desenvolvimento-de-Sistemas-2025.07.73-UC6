import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

print("BEM VINDO AO SISTEMA ESCOLA")

while True:
    print("Escolha uma opção do menu abaixo:")
    print('''
1. Cadastrar Aluno
2. Ver Alunos
0. Sair
''')
    op = input("Digite o número da opção desejada:")

    if op == "1":
        print("CADASTRO DE ALUNO")

        nome = input("Digite o nome do novo aluno:")

        cpf = input("Digite o cpf do novo aluno:")

        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                password=DB_PASSWORD, port=DB_PORT, host=DB_HOST)

        cur = conn.cursor()

        cur.execute('''
INSERT INTO aluno (nome_aluno, cpf_aluno)
VALUES(%s, %s)
''', (nome, cpf))

        conn.commit()

        cur.close()
        conn.close()

    elif op == "2":
        print("LISTA DE ALUNOS")
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                                password=DB_PASSWORD, port=DB_PORT, host=DB_HOST)

        cur = conn.cursor()

        cur.execute('''
SELECT * FROM aluno;
''')

        resultado = cur.fetchall()

        cur.close()
        conn.close()

        print(resultado)
        print("ID || NOME || CPF")
        for aluno in resultado:
            print(f"{aluno[0]} || {aluno[1]} || {aluno[2]}")
            
    elif op == "0":
        print("Saindo do Programa...")
        break
    else:
        print("Digite uma opção válida!")

    input("DIGITE ENTER PARA CONTINUAR!")
