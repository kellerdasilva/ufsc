# Importar os módulos
import turtle, math

# Criar uma tartaruga e referenciá-la pelo nome "tarta"
tarta = turtle.Turtle()
tarta.speed(10)

# Definir o valor da variável "x"
x = 100

# Definir uma função para desenhar os beirais
def beiral():
    tarta.forward(x / 2)
    tarta.right(180)
    tarta.forward(x/2)

# Desenhar o corpo da casa (um retângulo)
tarta.forward(2*x)
tarta.left(90)
tarta.forward(x)

tarta.right(135)
beiral()
tarta.left(45)

tarta.forward(2*x)

tarta.left(45)
beiral()
tarta.right(135)

tarta.forward(x)
tarta.left(90)

# Desenhar a porta
tarta.forward(x/3)
tarta.left(90)

tarta.forward(2*x/3)
tarta.right(90)
tarta.forward(x/3)
tarta.right(90)
tarta.forward(2*x/3)

# Desenhar a janela
tarta.up()  # anda sem riscar
tarta.left(90)
tarta.forward(x/4)
tarta.left(90)
tarta.forward(x/3)
tarta.down()  # volta a riscar

for i in range(4):
    tarta.forward(x/3)
    tarta.right(90)

tarta.up()
tarta.right(90)
tarta.forward(x/2)
tarta.down()

for i in range(4):
    tarta.forward(x/3)
    tarta.left(90)

tarta.up()
tarta.left(180)
tarta.forward(25)
tarta.right(90)
tarta.down()

# Desenhar o telhado
tarta.up()  # anda sem riscar
tarta.forward(2*x/3)
tarta.right(90)
tarta.forward(x/3 + x/2)
tarta.left(135)
tarta.down()  # volta a riscar

tarta.forward(x * math.sqrt(2))
tarta.left(90)
tarta.forward(x * math.sqrt(2))

# Indicar que a tarefa foi concluída
turtle.done()