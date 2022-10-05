# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

# import random

# num = int(input("Введите положительное целое число:\n"))
# if num <= 0:
#     print("Введено неправильное число")
# else:
#     num_list = []
#     for i in range(1, num + 1):
#         num_list.append(i)
#     print(f"Созданный список:\n{num_list}")
#     for i in range(num):
#         ran_pos = random.randint(0, num - 1)
#         num_list[i], num_list[ran_pos] = num_list[ran_pos], num_list[i]
#     print(f"Перемешанный список:\n{num_list}")

# Ещё вариант:

from random import randrange

num = int(input("Введите положительное целое число:\n"))
if num <= 0:
    print("Введено неправильное число")
else:
    nums_list = list(range(num))
    print(f"Созданный список:\n{nums_list}")

    for i in range(num):
        n_1 = randrange(num)
        n_2 = randrange(num)
        nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1]

    print(f"Перемешанный список:\n{nums_list}")