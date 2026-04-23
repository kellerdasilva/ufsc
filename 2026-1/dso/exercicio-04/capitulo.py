class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    # Número
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    # Título
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
