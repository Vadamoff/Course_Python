# 2. Напишите программу,
# которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

N = int(input("Введите число:\n"))
prod_set = []
for i in range(1, N + 1):
    prod = 1
    for j in range(1, i + 1):
        prod *= j
    prod_set.append(prod)
print(f"Набор произведений чисел от 1 до {N}:\n{prod_set}")