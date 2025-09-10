class Aluguel:
    def __init__(self, id, livro, cliente):

        self.id = id
        self.livro = livro
        self.cliente = cliente

    def mostrarInformacoes(self):
        print(f'''
Informações do Aluguel:
              
ID do Aluguel - {self.id}
''')
        self.cliente.mostrarInformacoes()
        self.livro.mostrarInformacoes()
