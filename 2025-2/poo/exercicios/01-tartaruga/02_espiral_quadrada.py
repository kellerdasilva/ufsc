# Importar o módulo Turtle
import turtle

# Criar uma variável para a tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(10)

for lado in range(0, 150, 5):
    tartaruga.forward(lado)
    tartaruga.right(90)

turtle.done()