import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math, numpy

WIN_W, WIN_H = 1000, 1000
#-0.001
GRAW = [0, 0]
SIM_SPEED = 0
square_pos = [0,0]
square_siz = 0.01


class particle:
    def __init__(self, pos, siz, acc, mass, color, static, lifetime, name):
        self.pos = [pos[0], pos[1]]
        self.acc = [acc[0], acc[1]]
        self.siz = siz
        self.color = color
        self.mass = mass
        self.static = static
        self.lifetime = lifetime
        self.starttime = pygame.time.get_ticks()
        self.name = name
     
    def draw(self,size_w, foll,target_pos):
        draw_square(self.pos, self.siz, size_w, self.color, foll, target_pos)
    def graw(self,particles):
        if  self.static == False:
            for i in range(len(particles)):
                cache_p = particles[i]
                if self.pos != cache_p.pos and cache_p.static != True:
                    cache_d = [cache_p.pos[0] - self.pos[0], cache_p.pos[1] - self.pos[1]]
                    dist = math.sqrt(cache_d[0]**2+cache_d[1]**2)
                    mass = self.mass / cache_p.mass
                    if dist != 0:
                        norm = [cache_d[0] / dist, cache_d[1] / dist]
                    else:
                        norm = [0,0]
                    self.acc[0] += norm[0] / (80 * mass)
                    self.acc[1] += norm[1] / (80 * mass)
    def tick(self, GRAW, particles):
        if  self.static == False:
            self.acc[0] += GRAW[0]
            self.acc[1] += GRAW[1]
        
        
    def move_tick(self):
        if  self.static == False:
            self.pos[0] += self.acc[0]
            self.pos[1] += self.acc[1]
    
    def colision(self, particles):
        if  self.static == False:
            for i in range(len(particles)):
                cache_p = particles[i]
                cache_d = [cache_p.pos[0] - self.pos[0], cache_p.pos[1] - self.pos[1]]
                dist = math.sqrt(cache_d[0]**2+cache_d[1]**2)
                if self.name != cache_p.name and dist <= 5 and cache_p.static != True:
                    particles.append(particle(self.pos, self.siz, [0,0], 15, [1,0,0], True, 500, len(particles)))
    
            



def draw_square(pos,size,size_w,color,foll,target_pos):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_QUADS)
    if foll == False:
        glVertex2f(pos[0]/(WIN_W*size_w) - size, pos[1]/(WIN_H*size_w) - size)
        glVertex2f(pos[0]/(WIN_W*size_w) + size, pos[1]/(WIN_H*size_w) - size)
        glVertex2f(pos[0]/(WIN_W*size_w) + size, pos[1]/(WIN_H*size_w) + size)
        glVertex2f(pos[0]/(WIN_W*size_w) - size, pos[1]/(WIN_H*size_w) + size)
    elif foll == True:
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) - size, (pos[1]-target_pos[1])/(WIN_H*size_w) - size)
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) + size, (pos[1]-target_pos[1])/(WIN_H*size_w) - size)
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) + size, (pos[1]-target_pos[1])/(WIN_H*size_w) + size)
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) - size, (pos[1]-target_pos[1])/(WIN_H*size_w) + size)
    glEnd()

def draw_all(particles,size_w, foll):
    glClear(GL_COLOR_BUFFER_BIT)
    draw_square(square_pos, square_siz,size_w, [0,1,0], foll, square_pos)
    for i in range(len(particles)):
        cache = particles[i]
        cache.draw(size_w,foll,square_pos)
    pygame.display.flip()


def sim_all(particles,GRAW):
    de = []
    for i in range(len(particles)):
        cache = particles[i]
        if cache.lifetime != "inf":
            if cache.starttime + cache.lifetime <= pygame.time.get_ticks(): 
                de.append(i)
    for i in range(len(de)):
        particles.pop(de[i]-i)
    de.clear

    for i in range(len(particles)):
        cache = particles[i]
        cache.graw(particles)
        cache.tick(GRAW,particles)
    for i in range(len(particles)):
        cache = particles[i]
        cache.colision(particles)
    for i in range(len(particles)):
        cache = particles[i]
        cache.move_tick()
    


def main():
    pygame.init()
    pygame.display.set_mode((WIN_W, WIN_H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Entites")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,1,-1,1,-1,1)
    glMatrixMode(GL_MODELVIEW)

    foll = False
    size_w = 1
    particles = []
    sim_speedt = 0
    last_spawn = pygame.time.get_ticks()
    last_butt = pygame.time.get_ticks()
    run = True
    clock = pygame.time.Clock()



    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        key = pygame.key.get_pressed()
        if key[K_EQUALS]:
            if size_w > 0.5:
                size_w -= 0.1
        if key[K_MINUS]:
            size_w += 0.1
        if key[K_LEFT]:
            square_pos[0] -= 4
        if key[K_RIGHT]:
            square_pos[0] += 4
        if key[K_UP]:
            square_pos[1] += 4
        if key[K_DOWN]:
            square_pos[1] -= 4
        if key[K_SPACE]:
            if last_spawn - pygame.time.get_ticks() < -300:
                particles.append(particle(square_pos, square_siz, [0,0], 1, [0,0,1], False, "inf", len(particles)))
                last_spawn = pygame.time.get_ticks()
        if key[K_b]:
            if last_spawn - pygame.time.get_ticks() < -300:
                particles.append(particle(square_pos, square_siz, [0,0], 15, [0,1,1], False, "inf", len(particles)))
                last_spawn = pygame.time.get_ticks()
        if key[K_c]:
            if last_spawn - pygame.time.get_ticks() < -300:
                particles.append(particle(square_pos, square_siz, [0,0], 15, [1,0,1], True, "inf", len(particles)  ))
                last_spawn = pygame.time.get_ticks()
        if key[K_f]:
            if last_butt - pygame.time.get_ticks() < -300:
                if foll == False:
                    foll = True
                else:
                    foll = False
                last_butt = pygame.time.get_ticks()

        
        
        if sim_speedt < SIM_SPEED:
            sim_speedt += 1
            draw_all(particles,size_w, foll)
            
        elif sim_speedt == SIM_SPEED:
            sim_speedt = 0
            draw_all(particles,size_w,foll)
            sim_all(particles, GRAW)
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()