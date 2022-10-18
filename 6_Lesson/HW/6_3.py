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