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
    print(f"Список контактов:\n")
    print(info)
    return m.select()

def print_many_found(indexes, surnames, names, numbers, comments, operation):
    print(f"Контакты:\n")
    for i in range(len(indexes)):
        print(f"{indexes[i]}\n\
Фамилия: {surnames[i]}\n\
Имя: {names[i]}\n\
Телефон: {numbers[i]}\n\
Комментарий: {comments[i]}\n")
    return m.up_del_many(indexes, operation)

def print_found(index, surname, name, number, comment, operation):
    print(f"Контакт:\n")
    print(f"{index}\n\
Фамилия: {surname}\n\
Имя: {name}\n\
Телефон: {number}\n\
Комментарий: {comment}\n")
    if operation == 'u':
        return m.update(index, operation)
    elif operation == 'd':
        return m.delete(index)