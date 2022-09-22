# 3. Напишите программу,
# которая будет на вход принимать число N
# и выводить числа от -N до N.

N = int(input('Введите число:\n'))
if N > 0:
    for i in range(- N, N + 1):
        print(i, end=' ')
elif N < 0:
    for i in range(- N, N - 1, - 1):
        print(i, end=' ')