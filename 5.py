# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import sys

# Объявляем все глобальные переменные
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math

def drawCube(w, h, z):
    z = -z
    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, z)
    glVertex3f(-w, h, z)
    glVertex3f(w, h, z)
    glVertex3f(w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(-w, h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, -h, -z)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(-w, h, -z)
    glVertex3f(-w, h, z)
    glVertex3f(-w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(w, -h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, h, z)
    glVertex3f(w, -h, z)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(w, -h, -z)
    glVertex3f(w, -h, z)
    glVertex3f(-w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-w, h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, h, z)
    glVertex3f(-w, h, z)
    glEnd()
    
    
pygame.init()
display = (1200, 900)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
glEnable(GL_BLEND)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [1,1,1, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1,1,1, 1])

glEnable(GL_LIGHT1)
glLightfv(GL_LIGHT1, GL_AMBIENT, [1,1,1, 1])
glLightfv(GL_LIGHT1, GL_SPECULAR, [1,1,1,1])



glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

pygame.mouse.set_visible(False)
up_down_angle = 0.0
paused = False
run = True

ambient = (0,1,1,1)

rotation = 0
x = 1
z=0
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 5)
#4 строки для освещения
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0,GL_POSITION,(5,0,0))
glEnable(GL_LIGHT1)
glLightfv(GL_LIGHT1,GL_POSITION,(0,0,5))
glLightfv(GL_LIGHT0,GL_SPECULAR,(0.4, 0.7, 0.2))
glLightfv(GL_LIGHT1, GL_DIFFUSE, (0,0,1));
glutInit(sys.argv)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)

        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # mouseMove = pygame.mouse.get_rel()

        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()
        ms = 0.06
        # apply the movment
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, ms)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -ms)
        if keypress[pygame.K_d]:
            glTranslatef(-ms, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(ms, 0, 0)
       
        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

    # multiply the current matrix by the get the new view matrix and store the final vie matrix 
    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    # apply view matrix
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Clear the screen


    
    glPushMatrix()
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 1, 1, 0.2])
    glColor4f(0.5, 0.1, 0.1,1)
              
    if keypress[pygame.K_q]:  
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.1, 0.1, 0.1,0.1))
        glColor4f(0.1, 0.1, 0.1,0.1)
    
    glRotatef(rotation, 1, 0, 0)
    glTranslatef(1.5, 0, 0)
    
    
    drawCube(0.5, 0.5, 0.5)
    
    glTranslatef(-3, 0, 0)
    
    drawCube(0.5, 0.5, 0.5)    
    rotation += 1
    if rotation > 360:
        rotation = 0    

    glPopMatrix()

    pygame.display.flip() #Update the screen
    pygame.time.wait(10)

pygame.quit()
