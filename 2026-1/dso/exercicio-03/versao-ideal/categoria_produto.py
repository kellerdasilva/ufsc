class CategoriaProduto:
    def __init__(self, titulo):
        self._titulo = titulo
    
    # Título
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
