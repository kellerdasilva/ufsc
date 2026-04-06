# Exercício 02

class Livro:
    def __init__(self, codigo, titulo, resumo, autor, protagonista, genero, faixa_etaria):
        self.codigo = codigo
        self.titulo = titulo
        self.resumo = resumo
        self.autor = autor
        self.protagonista = protagonista
        self.genero = genero
        self.faixa_etaria = faixa_etaria
    
    # Código
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
    
    # Título
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        self._codigo =valor
        
    
    # Resumo
    # Autor
    # Protagonista
    # Gênero
    # Faixa etária