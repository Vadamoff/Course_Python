import model_print as mp

contacts = {"Фамилия": [], "Имя": [], "Телефон": [], "Комментарий": []}

def import_db(data):
    global contacts
    contacts = data
    return mp.print_info(contacts)