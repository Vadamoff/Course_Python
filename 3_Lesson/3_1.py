#1. Задайте список, состоящий из произвольных чисел,
# количество задаёт пользователь.
# Напишите программу, которая определит,
# присутствует ли в заданном списке число,
# полученное от пользователя.

from random import sample

def num_in_list (count, num):
    if count < 0:
        return "Количество чисел в списке задано неверно"
    num_list = sample(range(1, count * 2), count)
    print(num_list)
    if num in num_list:
        return "В заданном списке введённое число присутствует"
    return "В заданном списке введённое число не присутствует"

print(num_in_list(int(input("Введите количество чисел в списке:\n")), int(input("Введите положительное число:\n"))))