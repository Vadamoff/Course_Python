# Найдите корни квадратного уравнения
# Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python.
# Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt

def roots(a, b, c):
    if a == 0:
        print("Число a не должно быть равно 0")
    else:
        d = b ** 2 - 4 * a * c
        with open("roots.txt", "a", encoding="utf-8") as r:
            r.write(f"({a})x² + ({b})x + ({c}) = 0\n")
            if d > 0:
                r.write(f"{round((- b + sqrt(d)) / (2 * a), 2)}\n")
                r.write(f"{round((- b - sqrt(d)) / (2 * a), 2)}\n")
            elif d == 0:
                r.write(f"{round((- b) / (2 * a), 2)}\n")
            else:
                r.write("Корней нет\n")

for i in range(3):
    roots(int(input("Введите число a:\n")), int(input("Введите число b:\n")), int(input("Введите число c:\n")))