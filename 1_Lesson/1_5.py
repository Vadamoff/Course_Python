# 5. Напишите программу,
# которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Введите число:\n'))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print(f'{num} кратно 5 и 10 или 15, но не 30')
else:
    print(f'{num} не кратно 5 и 10 или 15, или кратно 30')