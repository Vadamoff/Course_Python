# 1. Напишите программу,
# которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

num_1 = int(input('Введите 1 число:'))
num_2 = int(input('Введите 2 число:'))
if num_1 == num_2 ** 2:
    print(f'{num_1} является квадратом {num_2}')
elif num_2 == num_1 ** 2:
    print(f'{num_2} является квадратом {num_1}')
else:
    print('Ни одно число не является квадратом другого')