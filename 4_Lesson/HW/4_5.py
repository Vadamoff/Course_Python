# Даны два файла,
# в каждом из которых находится запись многочленов.
# Задача - сформировать файл,
# содержащий сумму многочленов.

# def count_lines(file):
#     lines = 0
#     with open(file, "r", encoding="utf-8") as p:
#         for line in p:
#             lines += 1
#     # print(lines)
#     return lines

def sum_polynoms(f_1, f_2, len):
    with open(f_1, "r", encoding="utf-8") as p_1, \
        open(f_2, "r", encoding="utf-8") as p_2, \
            open("sum_polynoms.txt", "a", encoding="utf-8") as sum_p:
        for i in range(len):
            p_1_line = p_1.readline().replace(" = 0", "")
            p_2_line = p_2.readline().replace(" = 0", "")
            sum_p.write(f"{p_1_line} + {p_2_line} = 0\n")

if len(open("polynom_1.txt").readlines()) != len(open("polynom_2.txt").readlines()):
    print("Файлы содержат различное количество строк")
else:
    sum_polynoms("polynom_1.txt", "polynom_2.txt", len(open("polynom_1.txt").readlines()))

# Вариант

# from random import choice

# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()

#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")

# # poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")