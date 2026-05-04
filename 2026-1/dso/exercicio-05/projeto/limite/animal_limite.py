from entidade import Cachorro, Gato, Canarinho

class AnimalLimite:
    def __init__(self):
        self.cachorro = None
        self.gato = None
        self.canarinho = None
    
    def criar_cachorro(self):
        self.cachorro = Cachorro()
        return self.cachorro
    
    def criar_gato(self):
        self.gato = Gato()
        return self.gato
    
    def criar_canarinho(self, tamanho_passo, altura_voo):
        self.canarinho = Canarinho(tamanho_passo, altura_voo)
        return self.canarinho
    
    def executar_mover(self, animal):
        return animal.mover()
    
    def executar_produzir_som(self, animal):
        return animal.produzir_som()
    
    def cachorro_latir(self):
        if self.cachorro:
            return self.cachorro.latir()
        return "Nenhum cachorro criado"
    
    def gato_miar(self):
        if self.gato:
            return self.gato.miar()
        return "Nenhum gato criado"
    
    def canarinho_cantar(self):
        if self.canarinho:
            return self.canarinho.cantar()
        return "Nenhum canarinho criado"