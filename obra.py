class Obra :

    def __init__(self, nome, local, status, codigo = None) :
        self.codigo = codigo
        self.nome = nome
        self.local = local
        self.status = status