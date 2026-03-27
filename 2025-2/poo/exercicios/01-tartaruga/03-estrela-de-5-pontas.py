# Importar o módulo Turtle
import turtle

# Criar uma variável para a tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(5)

# Desenhar a estrela de 5 pontas
for n in range(5):
    tartaruga.forward(100)
    tartaruga.left(144)

turtle.done()