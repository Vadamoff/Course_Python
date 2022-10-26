# Написать функцию,
# аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def dictionary(text: str) -> dict:
    dict = {}
    names = sorted(text.split())
    for name in names:
        k = name[0].upper()
        v = name.capitalize()
        if k in dict:
            dict[k] += [v]
        else:
            dict[k] = [v]
    return dict

print(dictionary(input("Введите имена через пробел:\n")))

# 2 вариант

# from itertools import groupby

# def thesaurus(*args):
#     if "" not in args:
#         return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
#     return "Error"

# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))

# 3 вариант

# def thesaurus(*args):
#     if "" not in args:
#         return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
#     return "Error"

# thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
#           'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')