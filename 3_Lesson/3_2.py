# 2. Задайте список, состоящий из произвольных слов,
# количество задаёт пользователь.
# Напишите программу,
# которая определит индекс второго вхождения строки в списке,
# либо сообщит, что её нет.

from random import choices

def word_list(count, word):
    new_list = []
    for i in range(count):
        symbol = choices(word, k = 3)
        new_list.append("".join(symbol))
    return new_list

def list_find(list_in, key):
    if list_in.count(key) > 1:
        first = list_in.index(key)
        print(list_in.index(key, first + 1))
    else:
        print("No")

result = word_list(20, "abc")
print(result)
list_find(result, input("Введите слово для поиска:\n"))