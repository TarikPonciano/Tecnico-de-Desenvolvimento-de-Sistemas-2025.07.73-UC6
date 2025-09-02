import psycopg2
from conexaoDB import ConexaoDB


class VendaDAO(ConexaoDB):
    def __init__(self, conexao):
        super().__init__(conexao.dbname, conexao.host,
                         conexao.port, conexao.user, conexao.password)

    def criarVenda(self, idCliente):
        self.conectar()

        try:
            self.cursor.execute('''
    INSERT INTO venda (cliente_id) VALUES (%s) RETURNING id_venda;
    ''', (idCliente,))
            self.conn.commit()
            idVenda = self.cursor.fetchone()
        except Exception as e:
            print("Erro de Cadastro de Venda:", e)
            self.conn.rollback()
            idVenda = None

        self.desconectar()

        return idVenda
