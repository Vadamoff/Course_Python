from os import path
import menu as m
import database as db

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

def write(file: str, contacts: str):
    surname = contacts.get("Фамилия")
    name = contacts.get("Имя")
    number = contacts.get("Телефон")
    comment = contacts.get("Комментарий")
    xml = "<xml>\n"
    for i in range(len(surname)):
        xml += f"   <person>{i}\n"
        xml += f"       <surname>{surname[i]}</surname>\n"
        xml += f"       <name>{name[i]}</name>\n"
        xml += f"       <number>{number[i]}</number>\n"
        xml += f"       <comment>{comment[i]}</comment>\n"
        xml += f"   </person>\n"
    xml += "</xml>"
    with open(file, "w", encoding="utf-8") as f:
        f.write(xml)
    return m.select()