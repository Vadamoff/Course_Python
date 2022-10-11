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
    with open(f_1, "r", encoding="utf-8") as p_1, open(f_2, "r", encoding="utf-8") as p_2, open("sum_polynoms.txt", "a", encoding="utf-8") as sum_p:
        for i in range(len):
            p_1_line = p_1.readline().replace(" = 0", "")
            p_2_line = p_2.readline().replace(" = 0", "")
            sum_p.write(f"{p_1_line} + {p_2_line} = 0\n")

if len(open("polynom_1.txt").readlines()) != len(open("polynom_2.txt").readlines()):
    print("Файлы содержат различное количество строк")
else:
    sum_polynoms("polynom_1.txt", "polynom_2.txt", len(open("polynom_1.txt").readlines()))