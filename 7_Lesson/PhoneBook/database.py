import model_print as mp
import menu as m

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

def find_in_db(data, operation):
    global contacts
    surname = contacts.get("Фамилия")
    name = contacts.get("Имя")
    number = contacts.get("Телефон")
    comment = contacts.get("Комментарий")
    data_low = data.lower()
    surname_low = [item.lower() for item in surname]
    name_low = [item.lower() for item in name]
    number_low = [item.lower() for item in number]
    comment_low = [item.lower() for item in comment]
    result = []
    if data_low in surname_low:
        result = [i for i in range(len(surname_low)) if data_low == surname_low[i]]
    elif data_low in name_low:
        result = [i for i in range(len(name_low)) if data_low == name_low[i]]
    elif data_low in number_low:
        result = [i for i in range(len(number_low)) if data_low == number_low[i]]
    elif data_low in comment_low:
        result = [i for i in range(len(comment_low)) if data_low == comment_low[i]]
    else:
        print("Данные отсутствуют")
        return m.select()
    indexes = sorted(set(result))
    if len(indexes) > 1:
        surnames = []
        names = []
        numbers = []
        comments = []
        for item in indexes:
            surnames += surname[item]
            names += name[item]
            numbers += number[item]
            comments += comment[item]
        return mp.print_many_found(indexes, surnames, names, numbers, comments, operation)
    else:
        index = result[0]
        return mp.print_found(index, surname[index], name[index], number[index], comment[index], operation)

def update_data(index, data_type, new_data, operation):
    global contacts
    surname = contacts.get("Фамилия")
    name = contacts.get("Имя")
    number = contacts.get("Телефон")
    comment = contacts.get("Комментарий")
    if data_type == "surname":
        surname[index] = new_data
        return mp.print_found(index, surname[index], name[index], number[index], comment[index], operation)
    elif data_type == "name":
        name[index] = new_data
        return mp.print_found(index, surname[index], name[index], number[index], comment[index], operation)
    elif data_type == "number":
        number[index] = new_data
        return mp.print_found(index, surname[index], name[index], number[index], comment[index], operation)
    elif data_type == "comment":
        comment[index] = new_data
        return mp.print_found(index, surname[index], name[index], number[index], comment[index], operation)

def delete_data(index):
    global contacts
    surname = contacts.get("Фамилия")
    name = contacts.get("Имя")
    number = contacts.get("Телефон")
    comment = contacts.get("Комментарий")
    del surname[index]
    del name[index]
    del number[index]
    del comment[index]
    print(f"Информация о контакте безвозвратно удалена")
    return m.select()