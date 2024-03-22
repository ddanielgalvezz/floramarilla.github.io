from turtle import *
import colorsys
import math
import pygame

# Inicializar pygame y cargar la canción
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/galve/Downloads/Flor Amarilla/music/FloresAmarillas.mp3')  # Ruta de la canción

def draw_flower():
    speed(0.25)
    bgcolor("black")

    # Genera los pétalos
    goto(0, -40)
    h = 0

    for i in range(16):
        for j in range(18):
            c = colorsys.hsv_to_rgb(0.125, 1, 1)
            color(c)
            rt(90)
            circle(150-j*6, 90)
            lt(90)
            circle(150-j*6, 90)
            rt(180)
        circle(40, 24)

    # Genera la parte central de la flor
    color("black") 
    shape("turtle")
    fillcolor("brown")
    phi = 137.508 * (math.pi/ 180.0)

    for i in range (200):
        r = 4 * math.sqrt(i)
        theta = i*phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        penup()
        goto(x, y)
        setheading(i * 137.508)
        pendown()
        stamp()

# Función para dibujar el mensaje "Te amo" encima de la flor
def draw_message():
    penup()
    goto(0, 250)  # Ajustar posición encima de la flor
    color("yellow")  # Color del texto
    style = ('Arial', 20)  # Tipo de fuente y tamaño
    write('Te amo mi Dani hermoso', font=style, align='center')
    hideturtle()  # Oculta la tortuga después de escribir el mensaje

# Reproduce la canción
pygame.mixer.music.play()

# Dibuja la flor
draw_flower()

# Dibuja el mensaje
draw_message()

# Cierra la ventana cuando se presiona la 'X'
def close_window(x, y):
    pygame.mixer.music.stop()  # Detiene la música
    pygame.quit()  # Cierra pygame
    bye()  # Cierra la ventana

# Configura la acción de cierre de la ventana
onscreenclick(close_window)

done()
