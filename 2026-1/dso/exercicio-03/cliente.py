class Cliente:

    def __init__(self, nome, fone):
        self.__nome = nome
        self.__fone = fone

    # Nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    # Fone
    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, valor):
        self.__fone = valor
        
    """Insira aqui os demais metodos ... """
