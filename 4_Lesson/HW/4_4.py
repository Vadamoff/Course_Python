# Задана натуральная степень k.
# Сформировать случайным образом
# список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

from random import randrange, choice

def polynomial(k):
    if k <= 0:
        print("Степень k должна быть больше 0")
    else:
        new_list = []
        signs = "+-"
        for i in range(k + 1):
            coef = randrange(0, 10)
            if coef > 0:
                if i != k:
                    new_list.append(f"{coef}*x^{k - i}")
                    new_list.append(choice(signs))
                else:
                    new_list.append(f"{coef}")
        
        # print(*new_list, sep=' + ', end=' = 0\n')
        new_str = ' '.join(new_list)
        with open("polynomial.txt", "a", encoding="utf-8") as p:
                    p.write(f"{new_str} = 0\n")

for _ in range(3):
    polynomial(int(input("Задайте степень k:\n")))

# Вариант

# from random import choice

# def polynomial(num: int):
#     if num < 1:
#         return 0

#     poly = ""
#     num_list = range(0, 10)
    
#     with open("poly.txt", "a", encoding="utf-8") as my_f:
#         for i in range(num, 1, -1):
#             value = choice(num_list)
#             if value:
#                 poly += f"{value}*x^{i} {choice('+-')} "

#         value_1 = choice(num_list)
#         if value_1:
#             poly += f"{value_1}*x {choice('+-')} "
        
#         value_2 = choice(num_list)
#         if value_2:
#             poly += f"{value_2}"
        
#         my_f.write(f"{poly} = 0\n")

# for _ in range(3):
#     polynomial(int(input()))