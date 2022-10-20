from tkinter import N
import model_import as mi
import model_export as me

info = ""

def select():
    print("Выберите действие:\n\
    i - импортировать данные из файла\n\
    e - экспортировать данные в файл\n\
    q - выйти из программы")
    action = input()
    if action == 'i':
        return import_file()
    elif action == 'e':
        return export_file()
    elif action == 'q':
        return
    else:
        print("Введён неверный символ")
        return select()

def import_file():
    global info
    info = (mi.check(input(f"Укажите файл для импорта:\n")))
    print(info)
    return select()

def export_file():
    me.check(input(f"Укажите файл для экспорта:\n"))
    return select()