# Создайте программу для игры в "Крестики-нолики".
# Поле 3x3. Игрок - игрок, без бота.

def print_field(field: list):
    for row in field:
        for cell in row:
            if cell == 'O':
                print("{hollow red circle}", end='')
            elif cell == 'X':
                print("{cross mark}", end='')
            else:
                print(cell, end='')
        print()

def turn(field: list):
    t = input("Ваш ход. Выберите ячейку:\n")
    if t in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if t in field:
            condit(t, field)
        else:
            print("Ячейка уже занята")
            turn(field)
    else:
        print("Вы ввели неверный номер ячейки")
        turn(field)

def condit(t: str, field: list):
    i = int(t) // len(field)
    j = int(t) % len(field[i]) - 1
    field[i][j] = 'X'
    return field

def check_victory():
    
    return 

field = [['1', '2', '3'], \
         ['4', '5', '6'], \
         ['7', '8', '9']]

victory_combs = [['1', '2', '3'], \
                 ['4', '5', '6'], \
                 ['7', '8', '9'], \
                 ['1', '4', '7'], \
                 ['2', '5', '8'], \
                 ['3', '6', '9'], \
                 ['1', '5', '9'], \
                 ['3', '5', '7']]

print_field(field)
turn(field)
print_field(field)