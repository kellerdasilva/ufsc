import math

# Obter os dados (a, b, c)
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Calcular delta
delta = b ** 2 - 4*a*c

# Calcular as raízes
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

# Imprimir o resultado
print(f"As raízes reais são: {x1}, {x2}")
