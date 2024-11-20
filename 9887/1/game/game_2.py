import random

def create_area(height, width, fill_char):
    return [[fill_char for _ in range(width)] for _ in range(height)]

def display_area(area):
    for row in area:
        print("".join(row),)
    print()

def change_symbol(area, x, y, new_char):
    if 0 <= x < len(area) and 0 <= y < len(area[0]):
        area[x][y] = new_char

def main():
    height, width = 15, 15

    fill_char = "\033[1;37;47m▉▉▉\033[m"
    tree_char = "\033[1;32;42m▉⯭▉\033[m"
    ply_pos = [60, 60]
    ply_char = "\033[1;34;44m▉¤▉\033[m"
    
    area = create_area(height, width, fill_char)
    change_symbol(area, *ply_pos, ply_char)

    if ply_pos[0]>height:
        ply_pos[0] = height-2
    if ply_pos[1]>width:
        ply_pos[1] = width-2
    
    i = 60
    while i > 0:
        tree_pos = (random.randint(0, height), random.randint(0, width))
        change_symbol(area, *tree_pos, tree_char)
        i -= 1

    move_map = {
        "w": (-1, 0), # вверх
        "s": (1, 0), # вниз
        "a": (0, -1), # влево
        "d": (0, 1) # вправо
    }
    
    while True:
        change_symbol(area, *ply_pos, fill_char)
        inp = input("Введите команду (w/a/s/d): ").strip()
        print('\033[2J')
        
        if inp in move_map:
            # Получаем изменения координат
            delta = move_map[inp]
            new_pos = [ply_pos[0] + delta[0], ply_pos[1] + delta[1]]

            # Проверяем, можно ли двигаться
            if 0 <= new_pos[0] < height and 0 <= new_pos[1] < width and area[new_pos[0]][new_pos[1]] != tree_char:
                ply_pos = new_pos # Обновляем позицию игрока

        change_symbol(area, *ply_pos, ply_char)
        print('\033[2J')
        display_area(area)

main()