from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    # Código
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    # Título
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    # Ano
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    # Editora
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora
    
    # Autores
    @property
    def autores(self):
        return self.__autores.copy()
    
    # Incluir autor
    def incluir_autor(self, autor: Autor):
        # Verificar se o autor é nulo
        if autor is None:
            raise ValueError("Autor não pode ser nulo")
        
        # Verificar se o autor já está vinculado ao livro
        for a in self.__autores:
            if a.codigo == autor.codigo:
                raise ValueError(f"Autor com código {autor.codigo} já está vinculado a este livro")
        
        self.__autores.append(autor)
    
    # Excluir autor
    def excluir_autor(self, autor: Autor):
        # Verificar se o autor é nulo
        if autor is None:
            raise ValueError("Autor não pode ser nulo")
        
        # Verificar se o autor existe na lista
        for i, a in enumerate(self.__autores):
            if a.codigo == autor.codigo:
                del self.__autores[i]
                return
        
        raise ValueError(f"Autor com código {autor.codigo} não está vinculado a este livro")

    # Incluir capítulo
    def incluir_capitulo(self, numero: int, titulo: str):
        # Verificar se já existe capítulo com mesmo título
        for cap in self.__capitulos:
            if cap.titulo == titulo:
                raise ValueError(f"Capítulo com título {titulo} já consta neste livro")
        
        self.__capitulos.append(Capitulo(numero, titulo))

    # Excluir capítulo
    def excluir_capitulo(self, titulo: str):
        # Verificar se o capítulo existe
        for i, cap in enumerate(self.__capitulos):
            if cap.titulo == titulo:
                del self.__capitulos[i]
                return
        
        raise ValueError(f"Capítulo com título {titulo} não encontrado neste livro")

    # Buscar capítulo por título
    def find_capitulo_by_titulo(self, titulo: str):
        for cap in self.__capitulos:
            if cap.titulo == titulo:
                return cap
        
        return None
