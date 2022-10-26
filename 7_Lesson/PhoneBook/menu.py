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
    u - изменить запись\n\
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
    elif action == 'u':
        return find_data(action)
    elif action == 'd':
        return find_data(action)
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

def find_data(operation):
    data = input(f"Введите данные для поиска (фамилию, имя, номер телефона или комментарий)\n")
    return db.find_in_db(data, operation)

def up_del_many(indexes, operation):
    if operation == 'u':
        index = int(input("Введите порядковый номер контакта для внесения изменений:\n"))
        if index in indexes:
            return update(index, operation)
        else:
            print("Введён неверный номер")
            return up_del_many(indexes, action)
    elif operation == 'd':
        index = int(input("Введите порядковый номер контакта для удаления:\n"))
        if index in indexes:
            return delete(index)
        else:
            print("Введён неверный номер")
            return up_del_many(indexes, operation)

def update(index, operation):
    print("Куда внести изминения?\n\
    1 - фамилия\n\
    2 - имя\n\
    3 - номер телефона\n\
    4 - комментарий\n\
    --- --- --- --- ---\n\
    5 - вернуться в меню\n")
    action = int(input())
    if action == 1:
        data_type = "surname"
        return update_data(index, data_type, operation)
    elif action == 2:
        data_type = "name"
        return update_data(index, data_type, operation)
    elif action == 3:
        data_type = "number"
        return update_data(index, data_type, operation)
    elif action == 4:
        data_type = "comment"
        return update_data(index, data_type, operation)
    elif action == 5:
        return select()
    else:
        print("Введён неверный символ")
        return select()

def update_data(index, data_type, operation):
    if data_type == "surname":
        new_data = input(f"Введите новую фамилию:\n")
        return db.update_data(index, data_type, new_data, operation)
    elif data_type == "name":
        new_data = input(f"Введите новое имя:\n")
        return db.update_data(index, data_type, new_data, operation)
    elif data_type == "number":
        new_data = input(f"Введите новый номер телефона:\n")
        return db.update_data(index, data_type, new_data, operation)
    elif data_type == "comment":
        new_data = input(f"Введите новый комментарий:\n")
        return db.update_data(index, data_type, new_data, operation)

def delete(index):
    print(f"Информация о контакте будет безвозвратно удалена. Вы уверены?\n\
    y - да\n\
    n - нет")
    action = input()
    if action == 'y':
        return db.delete_data(index)
    elif action == 'n':
        return select()
    else:
        print("Введён неверный символ")
        return select()