# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве разделителя используйте пробел.

# num_line = input("Введите набор чисел:\n")
# num_list = [int(i.strip(".,:;!?+=*/|")) for i in num_line.split() if i.replace("-", "").isdigit()]
# print(f"Большее число: {max(num_list)}", end="  ")
# print(f"Меньшее число: {min(num_list)}")

# Вариант

# num_list = [i.strip(".,:;!?+=*/|") for i in input("Введите набор чисел:\n").split() if i.replace("-", "").isdigit()]
# print(f"Большее число: {max(num_list, key=int)}", end="  ")
# print(f"Меньшее число: {min(num_list, key=int)}")

# Развёрнутая запись варианта

# num_list = []
# for i in input("Введите набор чисел:\n").split():
#     if i.replace("-", "").isdigit():
#         num_list.append(i.strip(".,:;!?+=*/|"))
# print(f"Большее число: {max(num_list, key=int)}", end="  ")
# print(f"Меньшее число: {min(num_list, key=int)}")

# Ещё вариант

def check(str_list):
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace("-", "").isdigit():
            return []
    return str_list


def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print("The data is incorrect")
    return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))