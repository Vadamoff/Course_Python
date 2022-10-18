# Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Use comprehension.

from random import randrange

def create_list(count: int, range_from: int, range_to: int) -> list:
    if count >= 0 and 0 <= range_from < range_to:
        return [randrange(range_from, range_to + 1) for _ in range(count)]
    else:
        print("Заданы неверные параметры")

def large_than_prev(list_in: list) -> list:
    return [list_in[i + 1] for i in range(len(list_in) - 1) if list_in[i] < list_in[i + 1]]

num_list = create_list(int(input("Задайте количество элементов в списке:\n")), int(input("Задайте начало диапазона случайных чисел для элементов в списке:\n")), int(input("Задайте конец диапазона случайных чисел для элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Cписок c элементами исходного, значения которых больше предыдущего элемента:\n{large_than_prev(num_list)}")