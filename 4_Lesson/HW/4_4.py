# Задана натуральная степень k.
# Сформировать случайным образом
# список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

from random import randrange

def polynomial(k):
    if k <= 0:
        print("Степень k должна быть больше 0")
    else:
        new_list = []
        for i in range(k + 1):
            coef = randrange(0, 10)
            if coef > 0:
                if i != k:
                    new_list.append(f"{coef}*x^{k - i}")
                else:
                    new_list.append(f"{coef}")
        
        # print(*new_list, sep=' + ', end=' = 0\n')
        new_str = ' + '.join(new_list)
        with open("polynomial.txt", "a", encoding="utf-8") as p:
                    p.write(f"{new_str} = 0\n")

for i in range(3):
    polynomial(int(input("Задайте степень k:\n")))