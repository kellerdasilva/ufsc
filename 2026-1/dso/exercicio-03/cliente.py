class Cliente:

    def __init__(self, nome, fone):
        self._nome = nome
        self._fone = fone

    # Nome
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # Fone
    @property
    def fone(self):
        return self._fone
    
    @fone.setter
    def fone(self, valor):
        self._fone = valor
        
    """Insira aqui os demais metodos ... """
