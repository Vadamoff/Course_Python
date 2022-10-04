# 4. Задайте список из произвольных вещественных чисел,
# количество задаёт пользователь.
# Напишите программу,
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

from random import uniform

def create_list(count, range_from, range_to):
    if count >= 0 and 0 <= range_from < range_to:
        new_list = []
        for i in range(count):
            new_list.append(round(uniform(range_from, range_to + 1), 2))
        return new_list
    else:
        print("Заданы неверные параметры")

def diff_max_min_list(list_in):
    new_list = []
    for i in range(len(list_in)):
        new_list.append(round((list_in[i] % 1) * 100))
    print(f"Максимальное значение дробной части элементов:\n{max(new_list) / 100}")
    print(f"Минимальное значение дробной части элементов:\n{min(new_list) / 100}")
    diff = (max(new_list) - min(new_list)) / 100
    return diff

num_list = create_list(int(input("Задайте количество элементов в списке:\n")), float(input("Задайте начало диапазона случайных чисел для элементов в списке:\n")), float(input("Задайте конец диапазона случайных чисел для элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Разница между максимальным и минимальным значением дробной части элементов:\n{diff_max_min_list(num_list)}")