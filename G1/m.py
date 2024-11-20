import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math

WIN_W, WIN_H = 1000, 1000
#-0.001
GRAW = [0, 0]
SIM_SPEED = 8
square_pos = [0,0]
square_siz = 0.01

class particle:
    def __init__(self, pos, siz, acc):
        self.pos = [pos[0], pos[1]]
        self.acc = [acc[0], acc[1]]
        self.siz = siz
        print("st")
        
    def draw(self):
        draw_square(self.pos, 0.01)
    def tick(self, GRAW, particles):
        
        if (self.pos[1] <= -1 + self.siz):
            self.pos[1] = -1 + self.siz
            if self.acc[1] < 0:
                self.acc[1] = 0
        elif (self.pos[1] >= 1 - self.siz):
            self.pos[1] = 1 - self.siz
            if self.acc[1] > 0:
                self.acc[1] = 0
        else:
            self.pos[1] += self.acc[1]
            self.acc[1] += GRAW[1]
        #----------
        if (self.pos[0] <= -1 + self.siz):
            self.pos[0] = -1 + self.siz
            if self.acc[0] < 0:
                self.acc[0] = 0
        elif (self.pos[0] >= 1 - self.siz):
            self.pos[0] = 1 - self.siz
            if self.acc[0] > 0:
                self.acc[0] = 0
        else:
            self.pos[0] += self.acc[0]
            self.acc[0] += GRAW[0]
        

        for i in range(len(particles)):
            cache_p = particles[i]
            if self.pos != cache_p.pos:
                cache_d = [math.fabs(self.pos[0]) - math.fabs(cache_p.pos[0]), math.fabs(self.pos[1]) - math.fabs(cache_p.pos[1])]
                if self.pos[0] < cache_p.pos[0]:
                    self.acc[0] += math.fabs(cache_d[0] / 40)
                elif self.pos[0] > cache_p.pos[0]:
                    self.acc[0] -= math.fabs(cache_d[0] / 40)
                if self.pos[1] < cache_p.pos[1]:
                    self.acc[1] += math.fabs(cache_d[1] / 40)
                elif self.pos[1] > cache_p.pos[1]:
                    self.acc[1] -= math.fabs(cache_d[1] / 40)
                




        

def draw_square(pos,size):
    glBegin(GL_QUADS)
    glVertex2f(pos[0] - size, pos[1] - size)
    glVertex2f(pos[0] + size, pos[1] - size)
    glVertex2f(pos[0] + size, pos[1] + size)
    glVertex2f(pos[0] - size, pos[1] + size)
    glEnd()

def draw_all(particles):
    glClear(GL_COLOR_BUFFER_BIT)
    draw_square(square_pos, square_siz)
    for i in range(len(particles)):
        cache = particles[i]
        cache.draw()
    pygame.display.flip()


def sim_all(particles,GRAW):
    for i in range(len(particles)):
        cache = particles[i]
        cache.tick(GRAW, particles)


def main():
    pygame.init()
    pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Entites")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,1,-1,1,-1,1)
    glMatrixMode(GL_MODELVIEW)

    particles = []
    sim_speedt = 0
    last_spawn = pygame.time.get_ticks()
    run = True
    clock = pygame.time.Clock()



    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

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
            if last_spawn - pygame.time.get_ticks() < -300:
                particles.append(particle(square_pos, square_siz, [0,0]))
                last_spawn = pygame.time.get_ticks()
                print(last_spawn)

        
        
        if sim_speedt < SIM_SPEED:
            sim_speedt += 1
            draw_all(particles)
            
        elif sim_speedt == SIM_SPEED:
            sim_speedt = 0
            draw_all(particles)
            sim_all(particles, GRAW)
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()