import pygame, mouse, pyautogui, keyboard
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math

pygame.init()
display = (800, 800)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
size = pyautogui.size()
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
modif_k = 0.1
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0, 1, 0.5, 0])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric() 

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

class Material:
    def __init__(self, filepath):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
mouse.move(size[0]/2, size[1]/2)

up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                mouse.move(size[0]/2, size[1]/2)
        if not paused: 
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            mouse.move(size[0]/2, size[1]/2)   

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        #mouseMove = pygame.mouse.get_rel()
    
        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1]*0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()

        # apply the movment 
        if keyboard.is_pressed("w"):
            glTranslatef(0,0,modif_k)
        elif keyboard.is_pressed("s"):
            glTranslatef(0,0,-modif_k)
        if keyboard.is_pressed("a"):
            glTranslatef(modif_k,0,0)
        elif keyboard.is_pressed("d"):
            glTranslatef(-modif_k,0,0)
        if keyboard.is_pressed("q"):
            glTranslatef(0,modif_k,0)
        elif keyboard.is_pressed("e"):
            glTranslatef(0,-modif_k,0)

        # apply the left and right rotation
        glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix 
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        glColor4f(0.5, 0.5, 0.5, 1)
        glBegin(GL_QUADS)
        glVertex3f(-10, -10, -2)
        glVertex3f(10, -10, -2)
        glVertex3f(10, 10, -2)
        glVertex3f(-10, 10, -2)
        glEnd()

        glTranslatef(-1.5, 0, 0)
        glColor4f(0.5, 0.2, 0.2, 1)
        gluSphere(sphere, 1.0, 32, 16) 

        glTranslatef(3, 0, 0)
        glColor4f(0.2, 0.2, 0.5, 1)
        gluSphere(sphere, 1.0, 32, 16) 

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(1)

pygame.quit()
















