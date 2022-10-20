from os import path
import menu as m

def check(file: str):
    if path.exists(file):
        return write(file, m.info)
    else:
        print("Файла не существует. Создать?\n\
    y - да\n\
    n - нет")
        action = input()
        if action == 'y':
            return write(file, m.info)
        elif action == 'n':
            return m.select()
        else:
            print("Введён неверный символ")
            return m.select()

def write(file: str, content: str):
    with open(file, "w", encoding="utf-8") as f:
        words_to_del_list = ["Имя:", "Телефон:", "Комментарий:"]
        data = (';'.join(filter(lambda w: w not in words_to_del_list, content.split()))).split("Фамилия:;")
        for i in range(len(data)):
            f.write(f"{data[i]}\n")
    return m.select()