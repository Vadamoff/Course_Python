from os import path
import menu as m
import database as db

def check(file: str):
    if path.exists(file):
        return read(file)
    else:
        print("Файла не существует или указан неверный путь")
        return m.import_file()

def read(file: str):
    with open(file, "r", encoding="utf-8") as f:
        data = db.contacts
        for line in f:
            person = line.replace("\n", '').split(';')
            data["Фамилия"] += [person[0]]
            data["Имя"] += [person[1]]
            data["Телефон"] += [person[2]]
            data["Комментарий"] += [person[3]]
    return db.import_db(data)