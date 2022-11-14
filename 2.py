# Импортируем все необходимые библиотеки:
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *  
import sys

global xrot         # Величина вращения по оси x
global yrot         # Величина вращения по оси y
global ambient      # рассеянное освещение
global greencolor   # Цвет елочных иголок
global treecolor    # Цвет елочного стебля
global lightpos     # Положение источника освещения


# Процедура инициализации
def init():
    global xrot         # Величина вращения по оси x
    global yrot         # Величина вращения по оси y
    global ambient      # Рассеянное освещение
    
    global lightpos     # Положение источника освещения

    xrot = 0.0                          # Величина вращения по оси x = 0
    yrot = 0.0                          # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 1)        # Первые три числа цвет в формате RGB, а последнее - яркость
    greencolor = (0.2, 0.8, 0.0, 0.8)   # Зеленый цвет для иголок
    treecolor = (0.9, 0.6, 0.3, 0.8)    # Коричневый цвет для ствола
    lightpos = (1.0, 1.0, 1.0)          # Положение источника освещения по осям xyz

    glClearColor(0.5, 0.5, 0.5, 1.0)                # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Определяем границы рисования по горизонтали и вертикали
    glRotatef(0, 1.0, 0.0, 0.0)                   # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)                           # Включаем освещение
    glEnable(GL_LIGHT0)                             # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)     # Определяем положение источника света


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot -= 2.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot += 2.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        yrot += 2.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки


# Процедура перерисовки
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global treecolor

    glClear(GL_COLOR_BUFFER_BIT)                                # Очищаем экран и заливаем серым цветом
    glPushMatrix()                                              # Сохраняем текущее положение "камеры"
    glRotatef(xrot, 1.0, 0.0, 0.0)                              # Вращаем по оси X на величину xrot
    glRotatef(yrot, 0.0, 1.0, 0.0)                              # Вращаем по оси Y на величину yrot
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)                 # Источник света вращаем вместе с елкой

    
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.9, 0.6, 0.3, 1))
    glTranslatef(0, 0, 0)  
    glBegin(GL_POLYGON)
    posx,posy = 0,0
    sides = 42
    radius = 0.8
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)
    glEnd()
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 1, 1, 1))
    glBegin(GL_POLYGON)
    posx,posy = 0.3,0.2
    sides = 42
    radius = 0.1
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine) 
    glEnd()
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 1, 1, 1))
    glBegin(GL_POLYGON)    
    posx,posy = -0.3,0.2
    sides = 42
    radius = 0.1
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)    
    glEnd() 
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 1, 0, 1))
    glTranslatef(0, 0, 0)  
    glBegin(GL_POLYGON)
    posx,posy = 0.3,0.2
    sides = 42
    radius = 0.05
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)
    glEnd()
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 1, 0, 1))
    glTranslatef(0, 0, 0)  
    glBegin(GL_POLYGON)
    posx,posy = -0.3,0.2
    sides = 42
    radius = 0.05
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)
    glEnd()  
    
    #mordochka
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.1, 0.1, 0.1, 1))
    glTranslatef(0, 0, 0)  
    glBegin(GL_POLYGON)
    posx,posy = -0.08,-0.25
    sides = 42
    radius = 0.1
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)
    glEnd()
    glBegin(GL_POLYGON)
    posx,posy = 0.08,-0.25
    sides = 42
    radius = 0.1
    for i in range(1000):
        cosine = radius * math.cos(i*2*math.pi/sides)+posx
        sine = radius * math.sin(i*2*math.pi/sides)+posy
        glVertex2f(cosine,sine)
    glEnd() 
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 1))
    glTranslatef(0, -0.15, 0)    
    glBegin(GL_TRIANGLES)
    
    glVertex2f(0,-0.1)
    glVertex2f(0.1,0)
    glVertex2f(-0.1,0)    
    glEnd() 
    
    #уши
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.8, 0.6, 0.3, 1))
    glTranslatef(0, 0, 0)    
    glBegin(GL_TRIANGLES)
    
    glVertex2f(0.7,0.9)
    glVertex2f(0.6,0.5)
    glVertex2f(0.3,0.7)    
    glEnd()    
    
    glTranslatef(0, 0, 0)    
    glBegin(GL_TRIANGLES)
    
    glVertex2f(-0.7,0.9)
    glVertex2f(-0.6,0.5)
    glVertex2f(-0.3,0.7)    
    glEnd()
    
    glPopMatrix()                                               # Возвращаем сохраненное положение "камеры"
    glutSwapBuffers()                                           # Выводим все нарисованное в памяти на экран


# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(300, 300)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(50, 50)
# Инициализация OpenGl
glutInit(sys.argv)
# Создаем окно с заголовком "Happy New Year!"
glutCreateWindow(b"Happy New Year!")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)
# Вызываем нашу функцию инициализации
init()
# Запускаем основной цикл
glutMainLoop()
    