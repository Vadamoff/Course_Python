# 1. Напишите программу,
# которая принимает на вход число N
# и выдаёт последовательность из N членов.

# 1 Вариант

# N = int(input("Введите число:\n"))
# prog = 1
# for i in range(N):
#     print(prog, end=' ')
#     prog *= -3

# 2 Вариант

N = int(input("Введите число:\n"))
prog = -3
for i in range(N):
    print(prog ** i, end=' ')