# 5. Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

def negaFibonacci(n):
    a = 1
    b = 1
    new_list = [0]
    for i in range(n):
        new_list.append(a)
        new_list.insert(0, a * (-1) ** i)
        a, b = b, a + b
    return new_list

num = int(input("Задайте число:\n"))
print(f"Список чисел Фибоначчи:\n{negaFibonacci(num)}")