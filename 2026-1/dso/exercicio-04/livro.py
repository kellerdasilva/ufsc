from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        # Criar todos os atributos, incluindo as listas
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas
        pass

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    # ... Adicionar demais getters
    
    # ... Adicionar demais setters
    

    def incluir_autor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!
        pass

    def excluir_autor(self, autor: Autor):
        pass

    def incluir_capitulo(self, numero: int, titulo: str):
        # ... Nao permitir insercao de Capitulos duplicados!
        pass

    def excluir_capitulo(self, titulo: str):
        pass

    def find_capitulo_by_titulo(self, titulo: str):
        # Procura na lista de capitulos se existe um Capitulo com este titulo 
        # Se encontrar, retorna o Capitulo encontrado
        pass
