from os import path
import menu as m
import database as db

def check(file: str):
    if path.exists(file):
        return write(file, db.contacts)
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

def write(file: str, contacts: str):
    with open(file, "w", encoding="utf-8") as f:
        surname = contacts.get("Фамилия")
        name = contacts.get("Имя")
        number = contacts.get("Телефон")
        comment = contacts.get("Комментарий")
        for i in range(len(surname) - 1):
            f.write(f"{surname[i]};{name[i]};{number[i]};{comment[i]}\n")
        f.write(f"{surname[-1]};{name[-1]};{number[-1]};{comment[-1]}")
    return m.select()