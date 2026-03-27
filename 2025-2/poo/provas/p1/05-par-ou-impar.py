# Ler a quantidade N de valores a serem lidos
n = int(input())

# Ler os números
for i in range (n):
    num = int(input())
    
    # Conferir se o número é 0, e a sua paridade
    if (num == 0):
        resultado = 'NULL'
    elif (num % 2 == 0):
        resultado = 'EVEN'
    else:
        resultado = 'ODD'
        
    # Conferir o sinal
    if (num == 0):
        pass
    elif (num > 0):
        resultado += ' POSITIVE'
    else:
        resultado += ' NEGATIVE'
    
    # Entregar o resultado
    print(resultado)