# Дан список чисел.
# Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices

def create_list(count: int):
    if count >= 0:
        new_list = choices(range(count * 2), k=count)
        return new_list
    else:
        print("Заданы неверные параметры")

def list_sets(list_in: list):
    new_list = []
    for i in range(len(list_in)):
        temp = list_in[i]
        temp_list = [temp]
        for j in range(i + 1, len(list_in)):
            if list_in[j] > temp:
                temp = list_in[j]
                temp_list.append(temp)
        if len(temp_list) > 1:
            new_list.append(temp_list)
    return new_list

num_list = create_list(int(input("Задайте количество элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Список с возрастающими последовательностями:\n{list_sets(num_list)}")