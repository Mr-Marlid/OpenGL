import pygame
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math






def draw():
    glColor3f(0,0.2,0)
    glBegin(GL_QUADS)
    glVertex2f(-3, -2)
    glVertex2f(3, -2)
    glVertex2f(3, 2)
    glVertex2f(-3,2)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex2f(-3, -2)
    glVertex2f(-1.5, -2)
    glVertex2f(-1.5, 2)
    glVertex2f(-3, 2)
    glEnd()

    glBegin(GL_POLYGON)
    posx,posy = 0,0
    sides = 42
    radius = 1
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)


    glEnd()
    glColor3f(0,0.2,0)
    glBegin(GL_POLYGON)
    posx, posy = 0.25, 0.25
    sides = 20
    radius = 1
    for i in range(1000):
        cosine = radius * math.cos(i * 2 * math.pi / sides) + posx
        sine = radius * math.sin(i * 2 * math.pi / sides) + posy
        glVertex2f(cosine, sine)

    glEnd() 

    #Звезда
    
    glBegin(GL_TRIANGLES)
    glColor3f(1,1,1)
    glVertex2f(0.5,0.4)
    glVertex2f(0.2,0.5)
    glVertex2f(0.6,-0.1)

    glVertex2f(0.5,0.4)
    glVertex2f(0.9,0.2)
    glVertex2f(0.1,0.1)

    glVertex2f(0.65,0.3)
    glVertex2f(0.3,0.3)
    glVertex2f(0.7,0.6)

    glVertex2f(0.6, 0.2)
    glVertex2f(0.4, 0.4)
    glVertex2f(0.6, -0.1)





    glEnd()

 
def main():
    pygame.init()
    display = 500,500
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(80,display[0]/display[1],1,10)
    glTranslate(0.0,0.0,-5)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
#         22
main()
