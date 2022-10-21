from tkinter import N
import model_import as mi
import model_export_txt as metxt
import model_export_csv as mecsv
import model_export_xml as mexml
import model_export_html as mehtml
import model_print as mp
import database as db

def select():
    print("Выберите действие:\n\
    i - импортировать данные из файла\n\
    e - экспортировать данные в файл\n\
    v - посмотреть все записи\n\
    a - добавить запись\n\
    r - изменить запись\n\
    d - удалить запись\n\
    q - выйти из программы")
    action = input()
    if action == 'i':
        return import_file()
    elif action == 'e':
        return export_format()
    elif action == 'v':
        info = db.contacts
        return mp.print_info(info)
    elif action == 'a':
        return add_data()
    elif action == 'r':
        return select()
    elif action == 'd':
        return select()
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

def export_xml():
    mexml.check(input(f"Укажите файл для экспорта:\n"))
    return select()

def export_html():
    mehtml.check(input(f"Укажите файл для экспорта:\n"))
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
        return export_xml()
    elif action == 4:
        return export_html()
    else:
        print("Введён неверный символ")
        return select()

def add_data():
    surname = input(f"Введите фамилию:\n")
    name = input(f"Введите имя:\n")
    number = input(f"Введите номер телефона:\n")
    comment = input(f"Введите комментарий:\n")
    return db.add_to_db(surname, name, number, comment)