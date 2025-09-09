from Control.ConexaoDB import ConexaoDB
from Control.ClienteDAO import ClienteDAO
from Control.LivroDAO import LivroDAO
from Model.Livro import Livro
from Model.Cliente import Cliente
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

    return livros


def modificarLivro():
    # Ver e obter lista de livros
    # O usuário deverá escolher um livro da lista
    # Mostrar informações do livro escolhido
    # Pedir as novas informações
    # Modifica o livro escolhido
    # Envia o livro escolhido para LivroDAO e modificar o banco de dados

    livros = verListaLivros()

    idLivro = int(input("Digite o id do livro que deseja modificar: "))

    livroEscolhido = None
    for livro in livros:
        if livro.id == idLivro:
            livroEscolhido = livro
            break

    if not livroEscolhido:
        print("Livro escolhido inválido!")
        return

#     print(f'''
#     Informações do Livro:
#     ID - {livro.id}
#     Nome - {livro.nome}
# ''')
    livroEscolhido.mostrarInformacoes()

    novoTitulo = input("Digite o novo titulo: ") or livroEscolhido.titulo

    livroEscolhido.titulo = novoTitulo

    livroDAO.atualizarLivro(livroEscolhido)


def removerLivro():
    # Ver e obter lista de livros
    # Pedir para o usuário escolher um livro específico
    # Mostrar informações do livro na tela
    # Pedir confirmação para remoção
    # Enviar o livro para o LivroDAO remover do banco de dados

    livros = verListaLivros()

    idLivro = int(input("Digite o id do livro que deseja modificar: "))

    livroEscolhido = None
    for livro in livros:
        if livro.id == idLivro:
            livroEscolhido = livro
            break

    if not livroEscolhido:
        print("Não foi possível remover o livro. Id não encontrado!")
        return

    print("Você escolheu:")

    livroEscolhido.mostrarInformacoes()

    print("Deseja remover esse livro?")

    confirmacao = input("Sim ou Não:")

    if confirmacao == "Sim":
        livroDAO.removerLivro(livroEscolhido)
    else:
        print("Remoção cancelada... Voltando para menu principal...")


def verListaClientes():

    clientes = clienteDAO.consultarClientes()

    print("LISTA DE CLIENTES")

    print("ID | NOME")

    for cliente in clientes:
        print(f"{cliente.id} | {cliente.nome}")


def cadastrarCliente():

    print("CADASTRO DE CLIENTE")

    nome = input("Digite o nome do novo cliente: ")

    novoCliente = Cliente(None, nome)

    clienteDAO.cadastrarCliente(novoCliente)


def main():
    while True:
        print("Sistema Biblioteca")
        print('''
Menu:

1. Ver Livros
2. Cadastrar Livro
3. Modificar Livro
4. Remover Livro
              
5. Ver Clientes
6. Cadastrar Clientes

''')
        op = input("Digite o id do livro desejado: ")

        if (op == "1"):
            verListaLivros()
        elif (op == "2"):
            cadastrarLivro()
        elif (op == "3"):
            modificarLivro()
        elif (op == "4"):
            removerLivro()
        elif (op == "5"):
            verListaClientes()
        elif (op == "6"):
            cadastrarCliente()
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
