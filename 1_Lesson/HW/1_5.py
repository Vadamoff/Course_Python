# 5. Напишите программу,
# которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math

def Distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1 = int(input('Введите значение x1:\n'))
y1 = int(input('Введите значение y1:\n'))
x2 = int(input('Введите значение x2:\n'))
y2 = int(input('Введите значение y2:\n'))
print(f'Расстояние между точками:\n{round(Distance(x1, y1, x2, y2), 2)}')