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
        '''SELECT * FROM funcionario
        LEFT JOIN departamento ON departamento_id = id_departamento
           ORDER BY id_funcionario ASC;''', [])
    print(funcionarios)

    print("ID | NOME | CPF | SALÁRIO | CARGO | DEPARTAMENTO")
    for func in funcionarios:
        print(
            f"{func[0]} | {func[1]} | {func[2]} | R$ {func[3]} | {func[4]} | {func[7]}")


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


def removerFuncionario():

    verFuncionarios()

    idFuncionario = int(
        input("Digite o id do funcionário que deseja remover (0 = cancelar): "))

    if idFuncionario <= 0:
        print("Operação cancelada...")
    else:
        resultado = meuBanco.manipular('''
DELETE FROM funcionario
WHERE id_funcionario = %s;
''', (idFuncionario,))

        if resultado == "DEU CERTO!":
            print("Funcionário removido com sucesso!")
        else:
            print("Erro ao tentar remover funcionário!")


def atualizarFuncionario():
    verFuncionarios()

    idFuncionario = int(
        input("Digite o id do funcionário que deseja remover (0 = cancelar): "))

    if idFuncionario <= 0:
        print("Operação cancelada...")
    else:

        funcionario = meuBanco.consultar('''
SELECT * FROM funcionario
LEFT JOIN departamento ON departamento_id = id_departamento
WHERE id_funcionario = %s;
''', (idFuncionario,))

        if len(funcionario) == 0:
            print("Funcionário não encontrado!")
        else:
            print(f'''
Informações do Funcionário:
                  
ID: {funcionario[0][0]}
Nome: {funcionario[0][1]}
CPF: {funcionario[0][2]}
Salário: R$ {funcionario[0][3]}
Cargo: {funcionario[0][4]}
Departamento: {funcionario[0][7]}                
''')
    print("DEIXE O CAMPO VAZIO PARA MANTER A INFORMAÇÃO ORIGINAL")
    novoNome = input("Digite o novo nome: ") or funcionario[0][1]
    novoCPF = input("Digite o novo cpf: ") or funcionario[0][2]
    novoSalario = input("Digite o novo salario: ") or funcionario[0][3]
    novoCargo = input("Digite o novo cargo: ") or funcionario[0][4]
    verDepartamentos()
    novoDepartamento = input(
        "Digite o novo id de departamento: ") or funcionario[0][5]

    resultado = meuBanco.manipular('''
UPDATE funcionario
SET
nome_funcionario = %s,
cpf_funcionario = %s,
salario_funcionario = %s,
cargo_funcionario = %s,
departamento_id = %s
WHERE id_funcionario = %s;                              
''', (novoNome, novoCPF, float(novoSalario), novoCargo, int(novoDepartamento), idFuncionario))

    if resultado == "DEU CERTO!":
        print("Funcionário Atualizado com sucesso!")
    else:
        print("Falha ao atualizar funcionário.")


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


def removerDepartamento():
    verDepartamentos()

    idDepartamento = int(
        input("Digite o departamento que deseja remover (0=cancelar):"))

    # departamentos = meuBanco.consultar('''SELECT * FROM departamento WHERE id_departamento = %s;''', [idDepartamento])

    if idDepartamento <= 0:
        print("Você cancelou a operação...")
    # elif len(departamentos) == 0:
    #     print("Você escolheu um departamento inválido...")
    else:
        resultado = meuBanco.manipular('''
DELETE FROM departamento
WHERE id_departamento = %s;
''', (idDepartamento,))
        if resultado == "DEU CERTO!":
            print("Departamento excluído com sucesso!")
        else:
            print("Erro ao excluir departamento!")


def atualizarDepartamento():
    verDepartamentos()

    idDepartamento = int(
        input("Digite o id do departamento que deseja modificar (0=cancelar):"))

    if (idDepartamento <= 0):
        print("Você cancelou a operação...")
    else:
        departamento = meuBanco.consultar('''
SELECT * FROM departamento
WHERE id_departamento = %s;
''', (idDepartamento,))

        if len(departamento) == 0:
            print("Departamento não encontrado!")
        else:
            # Para simplificar o acesso aos atributos
            # departamento = departamento[0]

            print(f'''
Departamento Selecionado:

ID: {departamento[0][0]}
Nome: {departamento[0][1]}
''')

            # novoNome = input("Digite o novo nome (vazio=sem alteração):")

            # if not novoNome:
            #     novoNome = departamento[0][1]

            novoNome = input("Digite o novo nome: ") or departamento[0][1]

            resultado = meuBanco.manipular('''
UPDATE departamento
SET
nome_departamento = %s
WHERE id_departamento = %s
''', (novoNome, idDepartamento))

            if resultado == "DEU CERTO!":
                print("Alteração realizada com sucesso!")
            else:
                print("Erro ao realizar alteração...")


def menuFuncionarios():

    while True:
        print("MENU FUNCIONARIOS")
        print('''Escolha uma opção abaixo:
1. Ver Funcionários
2. Cadastrar Funcionário
3. Atualizar Funcionário
4. Remover Funcionário
0. Voltar para menu principal''')
        op = input("Digite o número da opção desejada: ")

        if op == "1":
            verFuncionarios()
        elif op == "2":
            cadastrarFuncionario()
        elif op == "3":
            atualizarFuncionario()
        elif op == "4":
            removerFuncionario()
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
3. Atualizar Departamento
4. Remover Departamento
0. Voltar para menu principal''')
        op = input("Digite o número da opção desejada: ")

        if op == "1":
            verDepartamentos()
        elif op == "2":
            cadastrarDepartamento()
        elif op == "3":
            atualizarDepartamento()
        elif op == "4":
            removerDepartamento()
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
