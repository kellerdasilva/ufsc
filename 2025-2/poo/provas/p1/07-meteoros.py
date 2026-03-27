while True:
    try:
        # Ler as coordenadas do terreno
        x1, y1, x2, y2 = [int(n) for n in input().split()]
    except EOFError:
        break
    
    # Verificar se as coordenadas são todas nulas
    if x1 == y1 == x2 == y2 == 0:
        break
    
    # Ler o número N de meteoritos a serem analisados
    n = int(input())
    contador_meteoritos = 0
    
    for i in range(n):
        n_teste = i
        
        # Ler as coordenadas do meteorito
        x, y = [int(m) for m in input().split()]
        
        # Conferir se o meteorito caiu dentro ou fora do terreno
        if (x < x1) or (x > x2) or (y > y1) or (y < y2):
            pass
        else:
            contador_meteoritos += 1
    
    # Retornar o resultado
    print(f'Teste {n_teste}\n{contador_meteoritos}')