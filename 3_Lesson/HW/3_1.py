# 1. Задайте список, состоящий из произвольных чисел,
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).

from random import sample

def create_list(count, range_from, range_to):
    if count >= 0 and 0 <= range_from < range_to:
        new_list = sample(range(range_from, range_to + 1), count)
        return new_list
    else:
        print("Заданы неверные параметры")

def sum_odd_pos_elements(list_in):
    sum = 0
    for i in range(0, len(list_in), 2):
        sum += list_in[i]
    return sum

num_list = create_list(int(input("Задайте количество элементов в списке:\n")), int(input("Задайте начало диапазона случайных чисел для элементов в списке:\n")), int(input("Задайте конец диапазона случайных чисел для элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Сумма элементов на нечётных позициях списка:\n{sum_odd_pos_elements(num_list)}")