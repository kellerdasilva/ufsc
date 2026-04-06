# Importar o módulo Turtle
import turtle

# Criar uma variável para a tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(20)

# Desenhar a espiral
for lado in range(50, 400):
    tartaruga.forward(lado)
    tartaruga.right(91)

turtle.done()