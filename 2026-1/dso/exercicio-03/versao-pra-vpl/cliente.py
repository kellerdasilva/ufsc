class Cliente:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    # Nome
    def nome(self):
        return self.nome
    
    def nome(self, nome):
        self.nome = nome

    # Fone
    def fone(self):
        return self.fone
    
    def fone(self, fone):
        self.fone = fone
