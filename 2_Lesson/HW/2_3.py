# 3. Задайте список из n чисел,
# заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.

n = int(input("Введите число:\n"))
num_list = []
sum = 0
for i in range(1, n + 1):
    form = round((1 + 1 / i) ** i)
    num_list.append(form)
    sum += form
print(f"Полученный список:\n{num_list}")
print(f"Сумма элементов списка:\n{sum}")