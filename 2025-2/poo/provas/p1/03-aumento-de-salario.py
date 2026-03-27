# Ler o salário
salario = float(input())

# Calcular o índice de reajuste em porcentagem
if (salario <= 400.00):
    percentual = 15
elif (salario <= 800.00):
    percentual = 12
elif (salario <= 1200.00):
    percentual = 10
elif (salario <= 2000.00):
    percentual = 7
elif (salario >= 2000.00):
    percentual = 4

# Calcular o valor do reajuste e do noov salário
reajuste = percentual / 100 * salario
salario_novo = salario + reajuste

# Entregar o resultado
print(f"Novo salario: {salario_novo:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %")