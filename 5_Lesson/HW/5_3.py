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

row_1 = ['1', '2', '3']
row_2 = ['4', '5', '6']
row_3 = ['7', '8', '9']
field = [row_1, row_2, row_3]

print_field(field)
turn(field)
print_field(field)