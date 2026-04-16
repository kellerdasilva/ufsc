from categoria_produto import CategoriaProduto
from cliente import Cliente

class Produto:
    def __init__(self, codigo, descricao, categoria_produto, quantidade, preco_unitario, cliente):
        self.codigo = codigo
        self.descricao = descricao
        self.categoria_produto = categoria_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.cliente = cliente
    
    # codigo
    def codigo(self):
        return self.codigo
    
    def codigo(self, codigo):
        self.codigo = codigo
        
    # descricao
    def descricao(self):
        return self.descricao
    
    def descricao(self, descricao):
        self.descricao = descricao
        
    # categoria_produto
    def categoria_produto(self):
        return self.categoria_produto
    
    def categoria_produto(self, categoria_produto):
        self.categoria_produto = categoria_produto
        
    # quantidade
    def quantidade(self):
        return self.quantidade
    
    def quantidade(self, quantidade):
        self.quantidade = quantidade
        
    # preco_unitario
    def preco_unitario(self):
        return self.preco_unitario
    
    def preco_unitario(self, preco_unitario):
        self.preco_unitario = preco_unitario
        
    # cliente
    def cliente(self):
        return self.cliente
    
    def cliente(self, cliente):
        self.cliente = cliente
    
    # Método para calcular o valor total de um produto
    def preco_total(self):
        return self.quantidade * self.preco_unitario
