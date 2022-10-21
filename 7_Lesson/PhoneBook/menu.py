from tkinter import N
import model_import as mi
import model_export_txt as metxt
import model_export_csv as mecsv
import model_print as mp
import database as db

def select():
    print("Выберите действие:\n\
    i - импортировать данные из файла\n\
    e - экспортировать данные в файл\n\
    v - посмотреть все записи\n\
    q - выйти из программы")
    action = input()
    if action == 'i':
        return import_file()
    elif action == 'e':
        return export_format()
    elif action == 'v':
        info = db.contacts
        return mp.print_info(info)
    elif action == 'q':
        return
    else:
        print("Введён неверный символ")
        return select()

def import_file():
    contacts = mi.check(input(f"Укажите файл для импорта:\n"))
    print(contacts)
    return select()

def export_txt():
    metxt.check(input(f"Укажите файл для экспорта:\n"))
    return select()

def export_csv():
    mecsv.check(input(f"Укажите файл для экспорта:\n"))
    return select()

def export_format():
    print("Выберите формат:\n\
    1 - txt\n\
    2 - csv\n\
    3 - xml\n\
    4 - html")
    action = int(input())
    if action == 1:
        return export_txt()
    elif action == 2:
        return export_csv()
    elif action == 3:
        return select()
    elif action == 4:
        return select()
    else:
        print("Введён неверный символ")
        return select()