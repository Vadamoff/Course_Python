# 1. Напишите программу,
# которая принимает на вход вещественное число
# и показывает сумму его цифр.

num_in = float(input("Введите число:\n"))
if num_in < 0:
    num_in *= -1
num_len = len(str(num_in))
num = num_in * 10 ** (num_len - 1)
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print(f"Сумма цифр числа:\n{int(sum)}")