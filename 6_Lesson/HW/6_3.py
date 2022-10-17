# Написать функцию,
# аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def dictionary(text: str) -> dict:
    dict = {}
    names = sorted(text.split())
    for name in names:
        if name[0] in dict:
            dict[name[0].upper()] += [name.capitalize()]
        else:
            dict[name[0].upper()] = [name.capitalize()]
    return dict

print(dictionary(input("Введите имена через пробел:\n")))