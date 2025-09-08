from Control.ConexaoDB import ConexaoDB
from Model.Livro import Livro


class LivroDAO(ConexaoDB):
    def __init__(self, conexao):
        super().__init__(conexao.dbname, conexao.host,
                         conexao.port, conexao.user, conexao.password)

    def cadastrarNovoLivro(self, novoLivro):
        self.manipular('''
INSERT INTO livro VALUES(default, %s);
''', (novoLivro.titulo,))

    def consultarLivros(self):
        dadosBrutos = self.consultar('''
SELECT * FROM livro
ORDER BY id_livro ASC;
''')
        livros = []

        for dado in dadosBrutos:
            livro = Livro(dado[0], dado[1])
            livros.append(livro)

        return livros
