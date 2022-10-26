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
    html = "<html>\n<head></head>\n<body>\n"
    for i in range(len(surname)):
        html += f"   <div>{i}\n"
        html += f"       <p>{surname[i]}</p>\n"
        html += f"       <p>{name[i]}</p>\n"
        html += f"       <p>{number[i]}</p>\n"
        html += f"       <p>{comment[i]}</p>\n"
        html += f"   </div>\n"
    html += "</body>\n</html>"
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)
    return m.select()