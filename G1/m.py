import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

WIN_W, WIN_H = 800, 800
GRAW = 10

square_pos = [0,0]
square_siz = 0.01

class square:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        self.acc = [0, 0]
        print(self.pos)
    def draw(self):
        draw_square(self.pos, 0.01)
    def tick(self, GRAW):
        self.pos[0] += self.acc[0]
        self.pos[1] += self.acc[1]
        self.acc[0] += GRAW

def draw_square(pos,size):
    glBegin(GL_QUADS)
    glVertex2f(pos[0] - size, pos[1] - size)
    glVertex2f(pos[0] + size, pos[1] - size)
    glVertex2f(pos[0] + size, pos[1] + size)
    glVertex2f(pos[0] - size, pos[1] + size)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Entites")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,1,-1,1,-1,1)
    glMatrixMode(GL_MODELVIEW)

    particles = []

    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        
        for i in range(len(particles)):
            cache = particles[i]
            cache.tick(GRAW)

        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            square_pos[0] -= 0.01
        if key[K_RIGHT]:
            square_pos[0] += 0.01
        if key[K_UP]:
            square_pos[1] += 0.01
        if key[K_DOWN]:
            square_pos[1] -= 0.01
        if key[K_SPACE]:
            particles.append(square(square_pos))
        
        glClear(GL_COLOR_BUFFER_BIT)
        draw_square(square_pos, square_siz)
        for i in range(len(particles)):
            cache = particles[i]
            cache.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()