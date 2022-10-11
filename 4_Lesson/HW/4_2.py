# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def primfacts(n):
    primfacts = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            primfacts.append(i)
            n //= i
        i += 1
    if n > 1:
        primfacts.append(n)
    return primfacts

N = int(input("Задайте натуральное число:\n"))
print(f"Список простых множителей {N}:\n{primfacts(N)}")

# Вариант

# def find_prime_nums(num):
#     pr_fact = []
#     di = 2
#     while num > 1:
#         if num % di == 0:
#             pr_fact.append(di)
#             num //= di
#         else:
#             di += 1
#     return pr_fact

# print(find_prime_nums(int(input())))