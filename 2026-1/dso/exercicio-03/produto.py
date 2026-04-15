class Produto:
    
    def __init__(self, codigo, descricao, categoria_produto, quantidade, preco_unitario, cliente):
        self._codigo = codigo
        self._descricao = descricao
        self._categoria_produto = categoria_produto
        self._quantidade = quantidade
        self._preco_unitario = preco_unitario
        self._cliente = cliente
    
    # codigo
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
        
    # descricao
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        
    # categoria_produto
    @property
    def categoria_produto(self):
        return self._categoria_produto
    
    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        self._categoria_produto = categoria_produto
        
    # quantidade
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade
        
    # preco_unitario
    @property
    def preco_unitario(self):
        return self._preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self._preco_unitario = preco_unitario
        
    # cliente
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente
    
    # Método para calcular o valor total de um produto
    def preco_total(self):
        return self._quantidade * self._preco_unitario
