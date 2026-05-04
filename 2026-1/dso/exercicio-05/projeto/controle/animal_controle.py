from limite import AnimalLimite

class AnimalControle:
    def __init__(self):
        self.boundary = AnimalLimite()
    
    def criar_cachorro(self):
        return self.boundary.criar_cachorro()
    
    def criar_gato(self):
        return self.boundary.criar_gato()
    
    def criar_canarinho(self, tamanho_passo, altura_voo):
        return self.boundary.criar_canarinho(tamanho_passo, altura_voo)
    
    def mover_animal(self, animal):
        return self.boundary.executar_mover(animal)
    
    def animal_produzir_som(self, animal):
        return self.boundary.executar_produzir_som(animal)
    
    def fazer_cachorro_latir(self):
        return self.boundary.cachorro_latir()
    
    def fazer_gato_miar(self):
        return self.boundary.gato_miar()
    
    def fazer_canarinho_cantar(self):
        return self.boundary.canarinho_cantar()
    
    def demonstrar_animais(self):
        resultados = []
        
        # Criar animais
        cachorro = self.criar_cachorro()
        gato = self.criar_gato()
        canarinho = self.criar_canarinho(5, 10)
        
        # Testar Cachorro
        resultados.append("=== CACHORRO ===")
        resultados.append(self.mover_animal(cachorro))
        resultados.append(self.animal_produzir_som(cachorro))
        resultados.append(self.fazer_cachorro_latir())
        
        # Testar Gato
        resultados.append("\n=== GATO ===")
        resultados.append(self.mover_animal(gato))
        resultados.append(self.animal_produzir_som(gato))
        resultados.append(self.fazer_gato_miar())
        
        # Testar Canarinho
        resultados.append("\n=== CANARINHO ===")
        resultados.append(self.mover_animal(canarinho))
        resultados.append(self.animal_produzir_som(canarinho))
        resultados.append(self.fazer_canarinho_cantar())
        
        return resultados