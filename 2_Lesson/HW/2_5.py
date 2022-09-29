# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

import random

num = int(input("Введите положительное целое число:\n"))
if num <= 0:
    print("Введено неправильное число")
else:
    num_list = []
    for i in range(1, num + 1):
        num_list.append(i)
    print(f"Созданный список:\n{num_list}")
    for i in range(num):
        # print(num_list[i])
        ran_pos = random.randint(0, num - 1)
        # print(num_list[ran_pos])
        num_list[i], num_list[ran_pos] = num_list[ran_pos], num_list[i]
        # print(num_list[i])
    print(f"Перемешанный список:\n{num_list}")