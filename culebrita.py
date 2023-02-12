import turtle
import time
import random

posponer = 0.1#evitar que el programa vaya muy rapido

#Configurando la ventana
ventana = turtle.Screen()#crear ventana
ventana.title('Juego Skanek | Amadeus')#colocando titulo
ventana.bgcolor('black')#colocando color
ventana.setup(width=600,height=600)#dimensiones de la ventana
ventana.tracer(0)#animaciones placenteras xd

#creando la cabeza de la serpiente(elemento)
head = turtle.Turtle()
head.speed(0)#
head.shape('square')#forma cuadrado
head.color('white')
head.penup()
head.goto(0,0)#posicion de la pantalla
head.direction='stop'#estableciando direccion

#creando comida randomico
comida = turtle.Turtle()
comida.speed(0)#
comida.shape('circle')#forma circulo
comida.color('red')
comida.penup()
comida.goto(0,100)#posicion de la pantalla




#funciones
#funcion para mover hacia arriba
def arriba():
    head.direction='up'
#funcion para mover hacia abajo
def abajo():
    head.direction='down'
#funcion para mover hacia la izquierda
def izquierda():
    head.direction='left'
#funcion para mover hacia la derecha
def derecha():
    head.direction='right'

def movHead():#aumenta y quita dependiendo las direcciones 
    if head.direction == 'up':#ir hacia arriba
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':#ir hacia abajo
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':#ir hacia izquirda
        x = head.xcor()
        head.setx(x-20)
    
    if head.direction == 'right':#ir hacia la derecha
        x = head.xcor()
        head.setx(x+20)

#conectar con el teclado
ventana.listen()#eventos del teclado
ventana.onkeypress(arriba,'Up')
ventana.onkeypress(abajo,'Down')
ventana.onkeypress(izquierda,'Left')
ventana.onkeypress(derecha,'Right')

#creando bucle
while True:
    ventana.update()
    #definir distancia entre 2 obajetos
    if head.distance(comida)<20:
        x = random.randint(-280,280)#crear un numero entero
        y =  random.randint(-280,280)
        comida.goto(x,y)  #actualizar la posion  
    movHead()
    time.sleep(posponer)

ventana.exitonclick()#evitar que se apague la pantalla solito