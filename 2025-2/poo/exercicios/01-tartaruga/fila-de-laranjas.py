# for raio in range(0, 60, razao):
    
#     bola(raio)
    
#     d = math.sqrt((2 * raio + razao) ** 2 - razao ** 2)
    
#     tarta.up()
#     tarta.forward(d)
#     tarta.down()

# Importar o módulo Turtle
import turtle

# Criar uma variável para a tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(20)
tartaruga.color("orange")
tartaruga.up()

# Desenhar a fila de laranjas
razao = 10

for n in range(0, 60, razao):
    # Desenhar a bola
    tartaruga.begin_fill()
    tartaruga.circle(razao)
    tartaruga.end_fill()
    
    # Andar até o ponto certo
    tartaruga.forward(razao + razao * 1.4)
    razao *= 1.5

turtle.done()