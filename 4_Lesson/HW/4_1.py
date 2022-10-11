# Вычислить число c заданной точностью d.

from decimal import Decimal

print(Decimal(input("Введите число:\n")).quantize(Decimal(input("Задайте точность:\n"))))