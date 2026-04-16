from categoria_produto import CategoriaProduto
from cliente import Cliente
from produto import Produto

categoria = CategoriaProduto("Eletrônicos")
cliente = Cliente("Lucas", "98877-6655")

produto = Produto(1, "Notebook", categoria, 2, 3500)
produto.cliente = cliente

print(produto.preco_total())