class Livro:
    def __init__(self, id, titulo):
        self.id = id

        if titulo:
            self.titulo = titulo
        else:
            self.titulo = "Sem Título"

    def mostrarInformacoes(self):
        print(f'''
INFORMAÇÕES DO LIVRO:
              
ID - {self.id}
NOME - {self.titulo}

''')
