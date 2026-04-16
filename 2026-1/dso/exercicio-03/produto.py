from categoria_produto import CategoriaProduto
from cliente import Cliente

class Produto:
    def __init__(self, codigo, descricao, categoria_produto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = 0
        self.__preco_unitario = 0.0
        self.__cliente = None
    
    # codigo
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    # descricao
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        
    # categoria_produto
    @property
    def categoria_produto(self):
        return self.__categoria_produto
    
    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        if not isinstance(categoria_produto, CategoriaProduto):
            raise TypeError("categoria_produto deve ser um CategoriaProduto")
        self.__categoria_produto = categoria_produto
        
    # quantidade
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
        
    # preco_unitario
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
        
    # cliente
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        if cliente is not None and not isinstance(cliente, Cliente):
            raise TypeError("cliente deve ser um Cliente ou None")
        self.__cliente = cliente
    
    # Método para calcular o valor total de um produto
    def preco_total(self):
        return self.__quantidade * self.__preco_unitario
