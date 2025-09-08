class Livro:
    def __init__(self, id, titulo):
        self.id = id

        if titulo:
            self.titulo = titulo
        else:
            self.titulo = "Sem Título"
