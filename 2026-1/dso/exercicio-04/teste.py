from autor import Autor
from editora import Editora
from livro import Livro
from biblioteca import Biblioteca
from capitulo import Capitulo

print("=== TESTANDO O SISTEMA ===\n")

# Criando editora
editora = Editora(1, "Editora Tech")
print(f"Editora criada: {editora.nome} (código: {editora.codigo})")

# Criando autores
autor1 = Autor(1, "João Silva")
autor2 = Autor(2, "Maria Oliveira")
print(f"Autores criados: {autor1.nome}, {autor2.nome}")

# Criando livro (com primeiro autor e primeiro capítulo)
livro1 = Livro(100, "Python Avançado", 2023, editora, autor1, 1, "Introdução ao Python")
print(f"\nLivro criado: {livro1.titulo} (código: {livro1.codigo})")

# Testando incluir autor
print("\n--- Testando incluir_autor ---")
livro1.incluir_autor(autor2)
print(f"Autor {autor2.nome} incluído com sucesso!")
print(f"Total de autores: {len(livro1.autores)}")

# Testando incluir autor duplicado
try:
    livro1.incluir_autor(autor1)
    print("ERRO: Incluiu autor duplicado")
except ValueError as e:
    print(f"Correto! Não permitiu incluir autor duplicado: {e}")

# Testando incluir capítulo
print("\n--- Testando incluir_capitulo ---")
livro1.incluir_capitulo(2, "Classes e Objetos")
livro1.incluir_capitulo(3, "Herança e Polimorfismo")
print("Capítulos incluídos com sucesso!")
print(f"Total de capítulos: {len(livro1.capitulos)}")

# Testando incluir capítulo duplicado
try:
    livro1.incluir_capitulo(4, "Classes e Objetos")
    print("ERRO: Incluiu capítulo duplicado")
except ValueError as e:
    print(f"Correto! Não permitiu incluir capítulo duplicado: {e}")

# Testando find_capitulo_by_titulo
print("\n--- Testando find_capitulo_by_titulo ---")
cap = livro1.find_capitulo_by_titulo("Herança e Polimorfismo")
if cap:
    print(f"Capítulo encontrado: {cap.numero} - {cap.titulo}")
else:
    print("Capítulo não encontrado")

# Testando excluir capítulo
print("\n--- Testando excluir_capitulo ---")
livro1.excluir_capitulo("Classes e Objetos")
print("Capítulo 'Classes e Objetos' excluído com sucesso!")
print(f"Total de capítulos restantes: {len(livro1.capitulos)}")

# Testando excluir capítulo inexistente
try:
    livro1.excluir_capitulo("Capítulo Inexistente")
    print("ERRO: Excluiu capítulo inexistente")
except ValueError as e:
    print(f"Correto! Não permitiu excluir capítulo inexistente: {e}")

# Testando biblioteca
print("\n--- Testando Biblioteca ---")
biblioteca = Biblioteca()

# Incluir livro
biblioteca.incluir_livro(livro1)
print("Livro incluído na biblioteca com sucesso!")

# Tentar incluir livro duplicado
try:
    biblioteca.incluir_livro(livro1)
    print("ERRO: Incluiu livro duplicado")
except ValueError as e:
    print(f"Correto! Não permitiu incluir livro duplicado: {e}")

# Listar livros
print(f"\nTotal de livros na biblioteca: {len(biblioteca.livros)}")
for livro in biblioteca.livros:
    print(f"  - {livro.titulo} ({livro.ano})")

# Excluir livro
biblioteca.excluir_livro(livro1)
print("\nLivro excluído da biblioteca com sucesso!")
print(f"Total de livros após exclusão: {len(biblioteca.livros)}")

print("\n=== TESTES CONCLUÍDOS COM SUCESSO! ===")