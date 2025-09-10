from Control.ConexaoDB import ConexaoDB
from Model.Aluguel import Aluguel
from Model.Livro import Livro
from Model.Cliente import Cliente


class AluguelDAO(ConexaoDB):
    def __init__(self, conexao):
        super().__init__(conexao.dbname, conexao.host,
                         conexao.port, conexao.user, conexao.password)

    def consultarAlugueis(self):

        dadosBrutos = self.consultar('''
Select id_aluguel, id_cliente, id_livro, nome_cliente, titulo_livro from aluguel
INNER JOIN cliente ON cliente_id = id_cliente
INNER JOIN livro ON livro_id = id_livro
ORDER BY id_aluguel ASC;
''')
        alugueis = []

        for dado in dadosBrutos:
            aluguel = Aluguel(dado[0], Livro(
                dado[2], dado[4]), Cliente(dado[1], dado[3]))
            alugueis.append(aluguel)

        return alugueis

    def cadastrarAluguel(self, aluguel):
        self.manipular('''
INSERT INTO aluguel
VALUES (default, %s, %s);
''', (aluguel.cliente.id, aluguel.livro.id))
