from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, tamanho_passo):
        self._tamanho_passo = tamanho_passo
    
    @property
    def tamanho_passo(self):
        return self._tamanho_passo
    
    @tamanho_passo.setter
    def tamanho_passo(self, tamanho_passo):
        self._tamanho_passo = tamanho_passo
    
    def mover(self):
        return f"ANIMAL: DESLOCOU {self._tamanho_passo}"
    
    @abstractmethod
    def produzir_som(self):
        pass