import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, random

WIN_W, WIN_H = 1000, 1000
#-0.5
GRAW = [0, -0.5]
square_pos = [0,0]
square_siz = 1


class particle:
    def __init__(self, pos, siz, speed, mass, color, lifetime, name, actor, static=[False,False,False,False]):
        self.pos = [pos[0], pos[1]]
        self.speed = [speed[0], speed[1]]
        self.siz = siz
        self.color = color
        self.mass = mass
        self.static_g = static[0]
        self.static_m = static[1]
        self.static_mbg = static[2]
        self.static_c = static[3]
        self.lifetime = lifetime
        self.starttime = pygame.time.get_ticks()
        self.name = name
        self.actor = actor
        self.timer = 0
     
    def draw(self,size_w, foll,target_pos,size_h):
        draw_square(self.pos, self.siz, size_w, self.color, foll, target_pos, size_h)
        self.timer -= 1
    def graw(self,particles):
        if  self.static_mbg == False:
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
                    self.speed[0] += norm[0] / (80 * (dist/100) * mass)
                    self.speed[1] += norm[1] / (80 * (dist/100) * mass)
    def tick(self, GRAW, particles):
        if  self.static_g == False:
            self.speed[0] += GRAW[0]
            self.speed[1] += GRAW[1]
    
    def actor_action(self, particles):
        if self.actor == "bomber":
            self.speed = [5,0]
            for i in range(len(particles)):
                cache_p = particles[i]
                if cache_p.actor == "ship" and self.timer <= 0:
                    if : (fabs(self.pos[0]) - fabs(cache_p.pos[0]))-cache_p.speed[0]*sqrt(2*(self.pos[1]-cache_p[1]))/fabs(GRAW)
                        self.timer = 1000
                        particles.append(particle(self.pos, 1, [0,0], 1, [1,1,1], "inf", len(particles), "bomb", [False,False,True,True]))
        if self.actor == "bomb":
            for i in range(len(particles)):
                cache_p = particles[i]
                if cache_p.actor == "ship":
                    if cache_p.pos[1] >= self.pos[1]:
                        self.static_g = True
                        self.speed = [0,0]
        if self.actor == "ship":
            self.speed = [-5,0]
        pass
        
    def move_tick(self):
        if  self.static_m == False:
            self.pos[0] += self.speed[0]
            self.pos[1] += self.speed[1]
    
    def colision(self, particles):
        if  self.static_c == False:
            for i in range(len(particles)):
                cache_p = particles[i]
                cache_d = [cache_p.pos[0] - self.pos[0], cache_p.pos[1] - self.pos[1]]
                dist = math.sqrt(cache_d[0]**2+cache_d[1]**2)
                
                if dist < 10*(self.siz + cache_p.siz) and self.name != cache_p.name and cache_p.static != True:
                    #particles.append(particle(self.pos, self.siz, [0,0], 15, [1,0,0], True, 1000, len(particles)))
                    """
                    norm = [cache_d[0] - dist, cache_d[1] - dist]
                    if self.speed[0] * norm[0] <= 0:
                        self.speed[0] += self.speed[0] * -1
                    if self.speed[1] * norm[1] <= 0:
                        self.speed[1] += self.speed[1] * -1
                    """

class UI:
    def __init__(self, pos, siz, color=[[1,0,0],[0,1,0]], action_=[False,False]):
        self.pos = [pos[0], pos[1]]
        self.siz = [siz[0], siz[1]]
        self.cur_color = [color[0][0], color[0][1], color[0][2]]
        self.color = [[color[0][0], color[0][1], color[0][2]],[color[1][0], color[1][1], color[1][2]]]
        self.action_ = [action_[0], action_[1]]
        self.pressed = False
    def draw_box(self):
        glColor3f(self.cur_color[0], self.cur_color[1], self.cur_color[2])
        glBegin(GL_QUADS)

        glVertex2f(self.pos[0] / WIN_W * 2 - 1, 1 - self.pos[1] / WIN_H * 2)
        glVertex2f((self.pos[0] + self.siz[0]) / WIN_W * 2 -1, 1 - self.pos[1] / WIN_H * 2)
        glVertex2f((self.pos[0] + self.siz[0]) / WIN_W * 2 -1, 1 - (self.pos[1] + self.siz[1]) / WIN_H * 2)
        glVertex2f(self.pos[0] / WIN_W * 2 - 1, 1 - (self.pos[1] + self.siz[1]) / WIN_H * 2)

        glEnd()
    def action(self, particles, mouse):
        if self.action_[0] != False:
            if self.action_[0] == "on_self":
                m = pygame.mouse.get_pos()
                if  m[0] >= self.pos[0] and m[0] <= self.pos[0]+self.siz[0] and m[1] >= self.pos[1] and m[1] <= self.pos[1]+self.siz[1]:
                    if self.action_[1] == "spawn":
                        if mouse[0] and self.pressed == False:
                            self.pressed = True
                            particles.append(particle(square_pos, 1, [0,0], 1, [1,0,1], False, 2000, len(particles)))
                        elif mouse[0] == False and self.pressed:
                            self.pressed = False
                    elif self.action_[1] == "clear":
                        if mouse[0] and self.pressed == False:
                            self.pressed = True
                            particles.clear()
                        elif mouse[0] == False and self.pressed:
                            self.pressed = False
                    else:
                        self.cur_color = [self.color[1][0], self.color[1][1], self.color[1][2]]
                else:
                    self.cur_color = [self.color[0][0], self.color[0][1], self.color[0][2]]

        


def draw_square(pos,size,size_w,color,foll,target_pos, size_h):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_QUADS)
    if foll == False:
        glVertex2f(pos[0]/(WIN_W*size_w) - size*0.01*size_h, pos[1]/(WIN_H*size_w) - size*0.01*size_h)
        glVertex2f(pos[0]/(WIN_W*size_w) + size*0.01*size_h, pos[1]/(WIN_H*size_w) - size*0.01*size_h)
        glVertex2f(pos[0]/(WIN_W*size_w) + size*0.01*size_h, pos[1]/(WIN_H*size_w) + size*0.01*size_h)
        glVertex2f(pos[0]/(WIN_W*size_w) - size*0.01*size_h, pos[1]/(WIN_H*size_w) + size*0.01*size_h)
    elif foll == True:
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) - size*0.01*size_h, (pos[1]-target_pos[1])/(WIN_H*size_w) - size*0.01*size_h)
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) + size*0.01*size_h, (pos[1]-target_pos[1])/(WIN_H*size_w) - size*0.01*size_h)
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) + size*0.01*size_h, (pos[1]-target_pos[1])/(WIN_H*size_w) + size*0.01*size_h)
        glVertex2f((pos[0]-target_pos[0])/(WIN_W*size_w) - size*0.01*size_h, (pos[1]-target_pos[1])/(WIN_H*size_w) + size*0.01*size_h)
    glEnd()

def draw_all(particles,size_w, foll, size_h, ui, mouse):
    glClear(GL_COLOR_BUFFER_BIT)
    draw_square(square_pos, square_siz,size_w, [0,1,0], foll, square_pos,size_h)
    for i in range(len(particles)):
        cache = particles[i]
        cache.draw(size_w,foll,square_pos,size_h)
    for i in range(len(ui)):
        cache = ui[i]
        cache.action(particles, mouse)
        cache.draw_box()
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
        cache.tick(GRAW,particles)
        cache.actor_action(particles)
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

    size_h = 1
    foll = False
    pause = False
    size_w = 1
    particles = []
    sim_speedt = 0
    last_spawn = pygame.time.get_ticks()
    last_butt = pygame.time.get_ticks()
    run = True
    clock = pygame.time.Clock()
    ui = []
    ui.append(UI([0,0], [500,200], color=[[0.9,0.9,0.9],[0.7,0.7,0.7]]))
    ui.append(UI([100,50], [100,100], color=[[0.7,0.7,0.7],[0.6,0.6,0.6]] ,action_=["on_self", "spawn"]))
    ui.append(UI([250,50], [100,100], color=[[0.7,0.7,0.7],[0.6,0.6,0.6]] ,action_=["on_self", "clear"]))

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        mouse = pygame.mouse.get_pressed()
        key = pygame.key.get_pressed()
        if key[K_EQUALS]:
            size_w /= 1.1
            size_h *= 1.1
        if key[K_MINUS]:
            size_w *= 1.1
            size_h /= 1.1
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
                particles.append(particle(square_pos, 1, [0,0], 1, [1,0,1], "inf", len(particles), "bomber", [True,False,True,True]))
                last_spawn = pygame.time.get_ticks()
        if key[K_b]:
            if last_spawn - pygame.time.get_ticks() < -300:
                particles.append(particle(square_pos, 1, [0,0], 1, [0,0,1], "inf", len(particles), "ship", [True,False,True,True]))
                last_spawn = pygame.time.get_ticks()
        if key[K_c]:
            if last_spawn - pygame.time.get_ticks() < -300:
                particles.append(particle(square_pos, 1, [0,0], 15, [1,0,1], True, "inf", len(particles)  ))
                last_spawn = pygame.time.get_ticks()
        if key[K_f]:
            if last_butt - pygame.time.get_ticks() < -300:
                if foll == False:
                    foll = True
                else:
                    foll = False
                last_butt = pygame.time.get_ticks()
        if key[K_p]:
            if last_butt - pygame.time.get_ticks() < -300:
                if pause == False:
                    pause = True
                else:
                    pause = False
                last_butt = pygame.time.get_ticks()

        
        
        if pause == False:
            sim_all(particles, GRAW)
        draw_all(particles,size_w, foll,size_h, ui, mouse)
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()