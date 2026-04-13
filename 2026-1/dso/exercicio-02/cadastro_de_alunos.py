# Criar uma classe "Aluno" com os atributos: nome, endereço, telefone, idade e matrícula.
class Aluno:
    def __init__(self, nome, endereco, telefone, idade, matricula):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.idade = idade
        self.matricula = matricula
    
    # Nome
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    # Endereço
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    # Telefone
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    # Idade
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Idade deve ser um número inteiro")
        self._idade = valor
    
    # Matrícula
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula (self, valor):
        self._matricula = valor
    
    # Métodos
    def mostra_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}\n")
    
    def faz_aniversario(self):
        self.idade += 1

# Instanciar objetos
aluno1 = Aluno("Lucas da Silva", "Saco dos Limões, Florianópolis", "48-92030-1930", 20, "32030")
aluno2 = Aluno("Luís Carlos de Oliveira", "Costeira do Pirajubaé, Florianópolis", "48-91935-1909", 33, "11935")
aluno3 = Aluno("João Paulo da Cruz", "Ipiranga, São José", "48-91949-1900", 27, "21949")

# Testar métodos
aluno1.mostra_dados()
aluno1.faz_aniversario()
aluno1.mostra_dados()