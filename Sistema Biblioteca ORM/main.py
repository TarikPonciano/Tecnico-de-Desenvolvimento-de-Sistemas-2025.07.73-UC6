from database import Base, engine, Session
from models import Livro
from datetime import date


def configurarBanco():
    Base.metadata.create_all(bind=engine)


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
        pass
    elif op == "2":
        pass
    elif op == "9":
        configurarBanco()
    elif op == "0":
        print("Saindo do Programa...")
        break
    else:
        print("Opção inválida!")

    input("TECLE ENTER PARA CONTINUAR.")
