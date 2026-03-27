# Ler o código e a quantidade do item
codigo, qtd = [int(v) for v in input().split()]

# Associar o código ao produto
match codigo:
    case 1:
        preco = 4.00
    case 2:
        preco = 4.50
    case 3:
        preco = 5.00
    case 4:
        preco = 2.00
    case 5:
        preco = 1.50

# Calcular o total a pagar
total_conta = preco * qtd

# Entregar o resultado
print(f'Total: R$ {total_conta:.2f}')