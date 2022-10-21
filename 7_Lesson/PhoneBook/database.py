import model_print as mp

contacts = {"Фамилия": [], "Имя": [], "Телефон": [], "Комментарий": []}

def import_db(data):
    global contacts
    contacts = data
    return mp.print_info(contacts)

def add_to_db(surname, name, number, comment):
    global contacts
    contacts["Фамилия"] += [surname]
    contacts["Имя"] += [name]
    contacts["Телефон"] += [number]
    contacts["Комментарий"] += [comment]
    return mp.print_info(contacts)