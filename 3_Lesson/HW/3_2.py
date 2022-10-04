# 2. Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

from random import sample

def create_list(count, range_from, range_to):
    if count >= 0 and 0 <= range_from < range_to:
        new_list = sample(range(range_from, range_to + 1), count)
        return new_list
    else:
        print("Заданы неверные параметры")

def pairs_prod_list(list_in):
    size = len(list_in)
    flex_size = size // 2 + size % 2
    new_list = []
    
    for i in range(size // 2):
        new_list.append(list_in[i] * list_in[size - 1 - i])

    new_list.append(list_in[flex_size - 1])

    return new_list

num_list = create_list(int(input("Задайте количество элементов в списке:\n")), int(input("Задайте начало диапазона случайных чисел для элементов в списке:\n")), int(input("Задайте конец диапазона случайных чисел для элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Новый список, составленый из произведений пар предыдущего списка:\n{pairs_prod_list(num_list)}")