# Создайте список из N натуральных чисел.
# Среди чисел не хватает одного,
# чтобы выполнялось условие
# A[i] - 1 = A[i-1].
# Найдите это число.

from random import choice

def create_list(count: int):
    if count >= 0:
        new_list = [i for i in range(count +1)]
        new_list.remove(choice(new_list))
        return new_list
    else:
        print("Заданы неверные параметры")

def find_num(list_in: list):
    for i in range(1, len(list_in)):
        if list_in[i] - 1 != list_in[i-1]:
            return list_in[i] - 1
    return "В списке пропусков нет"

num_list = create_list(int(input("Задайте количество элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Пропущенное число:\n{find_num(num_list)}")