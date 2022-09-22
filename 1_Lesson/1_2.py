# 2. Напишите программу,
# которая на вход принимает 5 чисел и находит максимальное из них.

max_num = 0
for i in range(5):
    num = int(input('Введите число:\n'))
    if num > max_num:
        max_num = num
print(f'Максимальное число:\n{max_num}')