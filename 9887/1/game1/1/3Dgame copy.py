import pygame, sys, keyboard, time, threading, random
from numpy import floor
from perlin_noise import PerlinNoise

import matplotlib.pyplot as plt








pygame.init()

screen = pygame.display.set_mode((800, 800))


def display_area(area):
    for i, row in enumerate(area):
        for j, char in enumerate(row):
            yield char, (i,j)

def change_symbol(area, x, y, new_char):
    if 0 <= x < len(area) and 0 <= y < len(area[0]):
        area[x][y] = new_char

def game_m(height,width,ply_pos, area):
    area
    tree_pos = [8, 17]
    tree_char = "t"
    ply_char = "p"

    buf = area[ply_pos[0]]
    buf1 = buf[ply_pos[1]]
    change_symbol(area, tree_pos[0], tree_pos[1], tree_char)
    change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
    if keyboard.is_pressed("ESC"):
        pygame.quit()
        sys.exit()

    for char, (i,j) in display_area(area):
        if char == -1:
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (155, 155, 155), r, width=0)
        elif char == 0:
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (100, 155, 100), r, width=0)
        elif char == "t":
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (0, 155, 0), r, width=0)
        elif char == "p":
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (0, 0, 155), r, width=0)
    pygame.display.update()
    change_symbol(area, ply_pos[0], ply_pos[1], buf1)
        
def move_ply(height, width, ply_pos):
    if keyboard.is_pressed("s"):
        ply_pos[0]+=1
    elif keyboard.is_pressed("w"):
        ply_pos[0]-=1
    if keyboard.is_pressed("d"):
        ply_pos[1]+=1
    elif keyboard.is_pressed("a"):
        ply_pos[1]-=1
    if ply_pos[0] > height-1:
        ply_pos[0] -= 1
    elif ply_pos[0] < 0:
        ply_pos[0] += 1
    if ply_pos[1] > width-1:
        ply_pos[1] -= 1
    elif ply_pos[1] < 0:
        ply_pos[1] += 1
    

def start_game():
    height, width = 80, 80
    ply_pos = [5, 27]
    area = gen_w(height, width, random.randint(1, 999999))
    while True:
        move_ply(height, width, ply_pos)
        game_m(height, width, ply_pos, area)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #time.sleep(0.1)

def gen_w(height, width, seed):
    noise = PerlinNoise(2,seed)
    amp = 1
    period = 24


    landscale = [[0 for i in range(width)] for i in range(height)]

    for position in range(width*height):
    # вычисление высоты y в координатах (x, z)
        x = floor(position / width)
        z = floor(position % height)
        y = floor(noise([x/period, z/period])*amp)
        landscale[int(x)][int(z)] = int(y)
    return(landscale)

    
#st = threading.Thread(target=start_game)
#th = threading.Thread(target=start_game)
#st.start()
#th.start()
start_game()
