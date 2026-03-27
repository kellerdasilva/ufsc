while True:
    # Ler as coordenadas do ponto
    x, y = [int(n) for n in input().split()]
    
    # Verificar se pelo menos uma das coordenadas é nula
    if (x == 0) or (y == 0):
        break
    # Verificar em qual quadrante o ponto se encontra
    elif (x > 0) and (y > 0):
        quadrante = 'primeiro'
    elif (x < 0) and (y > 0):
        quadrante = 'segundo'
    elif (x < 0) and (y < 0):
        quadrante = 'terceiro'
    else:
        quadrante = 'quarto'
    
    # Entregar o resultado
    print(quadrante)