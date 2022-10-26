from os import path
import menu as m

def check(file: str):
    if path.exists(file):
        print("Файл уже существует. Перезаписать?\n\
    y - да\n\
    n - нет")
        action = input()
        if action == 'y':
            return write(file, db.contacts)
        elif action == 'n':
            return m.select()
        else:
            print("Введён неверный символ")
            return m.select()
    else:
        print("Файла не существует. Создать?\n\
    y - да\n\
    n - нет")
        action = input()
        if action == 'y':
            return write(file, db.contacts)
        elif action == 'n':
            return m.select()
        else:
            print("Введён неверный символ")
            return m.select()