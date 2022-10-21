import menu as m

def print_info(contacts):
    info = ""
    surname = contacts.get("Фамилия")
    name = contacts.get("Имя")
    number = contacts.get("Телефон")
    comment = contacts.get("Комментарий")
    for i in range(len(surname)):
        info += f"Фамилия: {surname[i]}   Имя: {name[i]}\n\
Телефон: {number[i]}\n\
Комментарий: {comment[i]}\n\n"
    print(info)
    return m.select()