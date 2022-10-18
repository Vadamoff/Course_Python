# Написать функцию,
# аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def dictionary(text: str) -> dict:
    dict = {}
    names = sorted(text.split())
    for name in names:
        key = name[0].upper()
        value = name.capitalize()
        if key in dict:
            dict[key] += [value]
        else:
            dict[key] = [value]
    return dict

print(dictionary(input("Введите имена через пробел:\n")))