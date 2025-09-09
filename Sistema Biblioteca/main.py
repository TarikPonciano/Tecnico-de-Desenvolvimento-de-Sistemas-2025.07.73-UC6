from Control.ConexaoDB import ConexaoDB
from Control.LivroDAO import LivroDAO
from Model.Livro import Livro
import dotenv
import os


def cadastrarLivro():
    # Coletar informações do livro (main) -> VIEW
    # Agrupar as informações. Usar o modelo (Livro) -> MODEL
    # Enviar as informações. (LivroDAO) -> CONTROL

    print("CADASTRAR NOVO LIVRO")

    titulo = input("Digite o titulo do livro: ")

    novoLivro = Livro(None, titulo)

    livroDAO.cadastrarNovoLivro(novoLivro)


def verListaLivros():

    # Consultar o banco e recuperar lista de livros
    # Construir a lista de (objetos) livro
    # Imprimir os livros na tela

    livros = livroDAO.consultarLivros()

    print("LISTA DE LIVROS:")

    print("ID | TITULO")
    for livro in livros:
        print(f"{livro.id} | {livro.titulo}")


def main():
    while True:
        print("Sistema Biblioteca")
        print('''
Menu:

1. Ver Livros
2. Cadastrar Livro

''')
        op = input("Digite o id do livro desejado: ")

        if (op == "1"):
            verListaLivros()
        elif (op == "2"):
            cadastrarLivro()
        elif (op == "0"):
            print("Saindo do Programa...")
            break
        else:
            print("Escolha uma opção válida.")

        input("TECLE ENTER PARA CONTINUAR.")


if __name__ == "__main__":
    dotenv.load_dotenv(dotenv.find_dotenv())

    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    meuBanco = ConexaoDB(dbname=DB_NAME, host=DB_HOST,
                         port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
    livroDAO = LivroDAO(meuBanco)
    clienteDAO = ClienteDAO(meuBanco)
    main()
