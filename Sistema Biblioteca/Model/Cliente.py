class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def mostrarInformacoes(self):
        print(f'''
Informações do Cliente:

ID - {self.id}
Nome - {self.nome}

''')
