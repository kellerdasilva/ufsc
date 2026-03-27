# Leitura e mapeamento dos alfabetos 
alfabeto = input()
cifra = input()
mapeamento = dict(zip(cifra, alfabeto))

# Leitura do texto criptografado
texto_cripto = input()
texto = ''

for car in texto_cripto:
    if car in mapeamento:
        texto += mapeamento[car]
    else:
        texto += car

print(texto)