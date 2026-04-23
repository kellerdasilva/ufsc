from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    # Livros
    @property
    def livros(self):
        return self.__livros.copy()
    
    # Incluir livro
    def incluir_livro(self, livro: Livro):
        # Verificar se o livro é nulo
        if livro is None:
            raise ValueError(f"Livro não pode ser nulo")
        
        # Verificar se o livro já está na biblioteca
        for l in self.__livros:
            if l.codigo == livro.codigo:
                raise ValueError(f"Livro com código {livro.codigo} já está na biblioteca")
        
        self.__livros.append(livro)
        
    # Excluir livro
    def excluir_livro(self, livro: Livro):
        # Verificar se o livro é nulo
        if livro is None:
            raise ValueError(f"Livro não pode ser nulo")
        
        # Verificar se o livro existe na biblioteca
        for i, l in enumerate(self.__livros):
            if l.codigo == livro.codigo:
                del self.__livros[i]
                return
        
        raise ValueError(f"Livro com código {livro.codigo} não encontrado na biblioteca")