# Leitura dos valores
nome = input()
salario = float(input())
vendas = float(input())

# Cálculo da comissão e do total a receber
comissao = vendas * 0.15
total_a_receber = salario + comissao

# Entrega do total a receber
print(f"TOTAL = R$ {total_a_receber:.2f}")