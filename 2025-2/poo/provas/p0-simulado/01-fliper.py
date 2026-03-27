# Leitura dos valores de P e R
p, r = [int(w) for w in input().split()]

buraco = ""

# Definição das posições de P e R
if (0 <= p <= 1) and (0 <= r <= 1):
    if (p == 0):
        buraco = "C"
    elif (r == 0):
        buraco = "B"
    elif (r == 1):
        buraco = "A"
    else:
        buraco = "Erro"
else:
    buraco = "Erro"        

print(buraco)