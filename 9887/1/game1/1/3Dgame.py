import pygame, sys, keyboard, time, threading

pygame.init()

screen = pygame.display.set_mode((800, 800))

def create_area(height, width, fill_char):
    return [[fill_char for _ in range(width)] for _ in range(height)]

def display_area(area):
    for i, row in enumerate(area):
        for j, char in enumerate(row):
            yield char, (i,j)

def change_symbol(area, x, y, new_char):
    if 0 <= x < len(area) and 0 <= y < len(area[0]):
        area[x][y] = new_char

def main(height,width,ply_pos):
    fill_char = "f"
    tree_pos = [8, 17]
    tree_char = "t"
    ply_char = "p"
    area = create_area(height, width, fill_char)
    change_symbol(area, tree_pos[0], tree_pos[1], tree_char)
    change_symbol(area, ply_pos[0], ply_pos[1], ply_char)

    if keyboard.is_pressed("ESC"):
        pygame.quit()
        sys.exit()

    for char, (i,j) in display_area(area):
        if char == "f":
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (155, 155, 155), r, width=0)
        if char == "t":
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (0, 155, 0), r, width=0)
        if char == "p":
            r = pygame.Rect(j*10, i*10, 10, 10)
            pygame.draw.rect(screen, (0, 0, 155), r, width=0)
    pygame.display.update()
        
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
    print(ply_pos)

def init():
    height, width = 80, 80
    ply_pos = [5, 27]
    while True:
        move_ply(height, width, ply_pos)
        main(height, width, ply_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.1)


    
#st = threading.Thread(target=init)
#th = threading.Thread(target=init)
#st.start()
#th.start()
init()
