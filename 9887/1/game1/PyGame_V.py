import pygame, keyboard, sys, pyautogui, mouse
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

verticles_m1 = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
verticles_m2 = (
    (2, -1, 1),
    (2, -1, -1),
    (3, -1, 1),
    (3, -1, -1),
    (2.5, 1, 0)
)

edges_m1 = (
    (0, 1),
    (0, 2),
    (1, 3),
    (3, 2),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
)
edges_m2 = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

colors_m1 = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces_m1 = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
  
def move_ply(ply_pos, size,camera_old, modif_k, modif_m):
    dir = [camera_old[0], camera_old[1], 0]
    camera_now = [0, 0, 0]
    camera_mod = [0, 0, 0]
    if keyboard.is_pressed("w"):
        ply_pos[2] += modif_k
        glTranslatef(0,0,modif_k)
    elif keyboard.is_pressed("s"):
        ply_pos[2] -= modif_k
        glTranslatef(0,0,-modif_k)
    if keyboard.is_pressed("a"):
        ply_pos[0] += modif_k
        glTranslatef(modif_k,0,0)
    elif keyboard.is_pressed("d"):
        ply_pos[0] -= modif_k
        glTranslatef(-modif_k,0,0)
    if keyboard.is_pressed("q"):
        ply_pos[1] += modif_k
        glTranslatef(0,modif_k,0)
    elif keyboard.is_pressed("e"):
        ply_pos[1] -= modif_k
        glTranslatef(0,-modif_k,0)


    mosuse_pos = mouse.get_position()
    camera_mod[0] += (mosuse_pos[0] - size[0]/2)
    camera_mod[1] += (mosuse_pos[1] - size[1]/2)
    glRotatef(camera_mod[0],0, 1, 0)
    glRotatef(camera_mod[1],1, 0, 0)
    camera_mod[0] = np.radians(camera_mod[0])
    camera_mod[1] = np.radians(camera_mod[1])

    R_0 = np.array([
        [1,0,0],
        [0,np.cos(camera_mod[0]),-np.sin(camera_mod[0])],
        [0,np.sin(camera_mod[0]),-np.cos(camera_mod[0])]
        ])
    R_1 = np.array([
        [np.cos(camera_mod[1]),0,np.sin(camera_mod[1])],
        [0,1,0],
        [-np.sin(camera_mod[1]),0,np.cos(camera_mod[1])]
        ])
    R = np.dot(R_1, R_0)

    camera_now = np.dot(R, dir)
    
    #camera_now[0] += camera_old[0] + camera_mod[0]
    #camera_now[1] += camera_old[1] + camera_mod[1]

    print(camera_now)
    return(camera_now, ply_pos)

def Cube():
    glEnable(GL_DEPTH_TEST)
    glBegin(GL_QUADS)
    for surface in surfaces_m1:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors_m1[x])
            glVertex3fv(verticles_m1[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges_m2:
        for vertex in edge:
            glVertex3fv(verticles_m1[vertex])
    glEnd() 
def Triangle():
    glBegin(GL_LINES)
    for edge in edges_m1:
        for vertex in edge:
            glVertex3fv(verticles_m2[vertex])
    glEnd()


def main():
    size = pyautogui.size()
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    ply_pos = [0,0,0]
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    camera_rot = [0.0, 0.0]
    mouse.move(size[0]/2, size[1]/2)
    modif_k = 0.1
    modif_m = 1

    while True:
        camera_rot, ply_pos = move_ply(ply_pos, size, camera_rot, modif_k, modif_m)
        mouse.move(size[0]/2, size[1]/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if keyboard.is_pressed("ESC"):
            pygame.quit()
            sys.exit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        Triangle()
        pygame.display.flip()
        pygame.time.wait(1)


main() 


















