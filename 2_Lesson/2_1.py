# 1. Напишите программу,
# которая принимает на вход число N
# и выдаёт последовательность из N членов.

N = int(input("Введите число:\n"))
prog = 1
for i in range(1, N + 1):
    print(prog, end=' ')
    prog *= -3