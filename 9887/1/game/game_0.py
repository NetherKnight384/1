def create_area(height, width, fill_char):
    return [[fill_char for _ in range(width)] for _ in range(height)]

def display_area(area):
    for row in area:
        print("".join(row))
    print()

def change_symbol(area, x, y, new_char):
    if 0 <= x < len(area) and 0 <= y < len(area[0]):
        area[x][y] = new_char

def main():
    height, width = 10, 30
    fill_char = "█"
    tree_pos = [8, 17]
    tree_char = "⯭"
    ply_pos = [5, 27]
    ply_char = "¤"
    area = create_area(height, width, fill_char)
    change_symbol(area, tree_pos[0], tree_pos[1], tree_char)
    change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
    
    while 0<1:
        change_symbol(area, ply_pos[0], ply_pos[1], fill_char)
        inp = str(input())
        cash = (ply_pos[0], ply_pos[1])
        if inp == "w":
            ply_pos[0] = ply_pos[0] - 1
            if area[ply_pos[0]][ply_pos[1]] == tree_char:
                ply_pos[0] = ply_pos[0] + 1
            change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
        elif inp == "s":
            ply_pos[0] = ply_pos[0] + 1
            if area[ply_pos[0]][ply_pos[1]] == tree_char:
                ply_pos[0] = ply_pos[0] - 1
            change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
        elif inp == "a":
            ply_pos[1] = ply_pos[1] - 1
            if area[ply_pos[0]][ply_pos[1]] == tree_char:
                ply_pos[1] = ply_pos[1] + 1
            change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
        elif inp == "d":
            ply_pos[1] = ply_pos[1] + 1
            if area[ply_pos[0]][ply_pos[1]] == tree_char:
                ply_pos[1] = ply_pos[1] - 1
            change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
        else:
            change_symbol(area, ply_pos[0], ply_pos[1], ply_char)
        display_area(area)



main()
    
