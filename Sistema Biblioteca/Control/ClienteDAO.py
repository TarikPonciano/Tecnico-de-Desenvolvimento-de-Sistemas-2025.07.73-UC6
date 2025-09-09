from Control.ConexaoDB import ConexaoDB
from Model.Cliente import Cliente


class ClienteDAO(ConexaoDB):
    def __init__(self, conexao):
        super().__init__(conexao.dbname, conexao.host,
                         conexao.port, conexao.user, conexao.password)

    def cadastrarCliente(self, novoCliente):
        self.manipular('''
INSERT INTO cliente VALUES (default, %s);
''', (novoCliente.nome,))

    def consultarClientes(self):

        dadosBrutos = self.consultar('''
SELECT * FROM cliente
ORDER BY id_cliente ASC;
''')
        clientes = []

        for dado in dadosBrutos:
            cliente = Cliente(dado[0], dado[1])
            clientes.append(cliente)

        return clientes
