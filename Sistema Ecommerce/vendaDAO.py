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

    def cadastrarItensVenda(self, idVenda, produtosComprados):

        listaAtualizaEstoque = []
        listaInsereItem = []
        totalVenda = 0

        for produto in produtosComprados.values():
            itemEstoque = (produto["quantidade"], produto["id"])
            listaAtualizaEstoque.append(itemEstoque)

            itemProduto = (
                idVenda, produto["id"], produto["quantidade"], produto["preco"])
            listaInsereItem.append(itemProduto)

            totalVenda += produto["preco"] * produto["quantidade"]
        self.conectar()
        try:
            # Atualizar estoques dos produtos
            self.cursor.executemany('''
UPDATE produto
SET
estoque_produto = estoque_produto - %s
WHERE
id_produto = %s;
''', listaAtualizaEstoque)

        # Cadastrar os produtos no banco

            self.cursor.executemany('''
INSERT INTO item
VALUES(default, %s, %s, %s, %s);

''', listaInsereItem)

        # Atualizar total da venda

            self.cursor.execute('''UPDATE venda
                                SET total_venda = %s
                                WHERE id_venda = %s;''', (totalVenda, idVenda))

            self.conn.commit()
            resultado = True

        except Exception as e:
            print("Erro ao cadastrar venda:", e)
            self.conn.rollback()
            resultado = False

        self.desconectar()

        return resultado

    def removerVenda(self, idVenda):
        self.manipular('''DELETE FROM venda WHERE id_venda = %s''', idVenda)
