from os import path
import menu as m

def check(file: str):
    if path.exists(file):
        return read(file)
    else:
        print("Файла не существует или указан неверный путь")
        return m.import_file()

def read(file: str):
    with open(file, "r", encoding="utf-8") as f:
        info = ""
        for line in f:
            person = line.split(';')
            info += f"Фамилия: {person[0]}    Имя: {person[1]}\n\
Телефон: {person[2]}\n\
Комментарий: {person[3]}\n"
    return info