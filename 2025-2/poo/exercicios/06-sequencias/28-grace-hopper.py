while True:
    try:
        # Separar as palavras da frase
        frase = input().lower().split('-')
        
    except EOFError:
        break

    cobol = 'cobol'
    tem_bug = False

    # Comparar as letras
    for i in range(len(frase)):
        palavra = frase[i]
        if palavra[0] != cobol[i] and palavra[-1] != cobol[i]:
            tem_bug = True
            break

    # Imprimir o resultado
    print ('BUG' if tem_bug else 'GRACE HOPPER')