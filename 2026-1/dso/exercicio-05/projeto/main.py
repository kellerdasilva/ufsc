from controle import AnimalControle

def main():
    controle = AnimalControle()
    
    resultados = controle.demonstrar_animais()
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()