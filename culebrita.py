import turtle
import time
import random

posponer = 0.1#evitar que el programa vaya muy rapido

#marcador 
score = 0
high_score = 0


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

#cuerpo de la serpiente /Segmentos
segmento=[]

#creacion de textos
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Puntos: 0    High Score = 0', align='center', font = ('Courier', 24, 'normal'))

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

    #conliciones para los bordes(perder)
    if head.xcor() >280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #esconder segementos
        for segmentos in segmento:
            segmentos.goto(1000,1000)
        #limpiar lista de segmentos 
        segmento.clear()

        #resetear marcador
        score=0
        texto.clear()
        texto.write('Puntos: {}    High Score = {}'.format(score,high_score),
         align='center', font = ('Courier', 24, 'normal'))
    


    #definir distancia entre 2 obajetos
    if head.distance(comida)<20:
        x = random.randint(-280,280)#crear un numero entero
        y =  random.randint(-280,280)
        comida.goto(x,y)  #actualizar la posion 

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)#
        nuevo_segmento.shape('square')#forma cuadrado
        nuevo_segmento.color('grey')
        nuevo_segmento.penup()

        segmento.append(nuevo_segmento)
        #aumentar marcador
        score+=10
        if score>high_score:
            high_score=score
        texto.clear()
        texto.write('Puntos: {}    High Score = {}'.format(score,high_score),
         align='center', font = ('Courier', 24, 'normal'))
    
    #mover el cuerpo de la serpiente
    totalSeg = len(segmento)
    for index in range(totalSeg -1, 0, -1):
        x = segmento[index-1].xcor()
        y = segmento[index-1].ycor()
        segmento[index].goto(x,y)
    if totalSeg >0:
        x = head.xcor()
        y = head.ycor()
        segmento[0].goto(x,y)




    movHead()
    #colisiones con el cuerpo
    for segmentos in segmento:
        if segmentos.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction ='stop'

            #esconder los segmentos
            for segmentos in segmento:
                segmentos.goto(1000,1000)
            segmentos.clear()

            score=0
            texto.clear()
            texto.write('Puntos: {}    High Score = {}'.format(score,high_score),
            align='center', font = ('Courier', 24, 'normal'))
    

    time.sleep(posponer)

ventana.exitonclick()#evitar que se apague la pantalla solito