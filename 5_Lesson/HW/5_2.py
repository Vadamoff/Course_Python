# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from os import path
from itertools import groupby, starmap

def check(data):
    return path.exists(data)

# encode 1 вариант

# def encode(data: str):
#     encoding = ""
#     prev_char = ''
#     count = 1

#     if not data:
#         return "Файл пустой"

#     else:
#         for char in data:
#             if char != prev_char:
#                 if prev_char:
#                     encoding += str(count) + prev_char
#                 count = 1
#                 prev_char = char
#             else:
#                 count += 1
#         encoding += str(count) + prev_char
#         return encoding

# encode 2 вариант

def encode(data: str):
    chars = [str(len(list(g))) + k for k, g in groupby(data)]
    return ''.join(chars)

# decode 1 вариант

# def decode(data: str):
#     count = ""
#     decode = ""

#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += int(count) * char
#             count = ""
#     return decode

# decode 2 вариант

def decode(data: str):
    pairs = []
    count = ""

    for i in data.strip():
        if i.isdigit():
            count += i
        else:
            pairs.append([int(count), i])
            count = ""
    return "".join(starmap(lambda x, y: x * y, pairs))

# decode 3 вариант - не додумался... (

# def decode(data: str):
#     print([k for k, g in groupby(data) if k.isdigit()])

def read(file: str):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def write(file: str, content: str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

file_to_encode = input("Укажите файл с текстом для сжатия:\n")
if check(file_to_encode):
    print(f"Исходный текст:\n{read(file_to_encode)}")
    encoded_text = encode(read(file_to_encode))
    print(f"Сжатый текст:\n{encoded_text}")
else:
    print("Файла не существует или указан неверный путь")

comp_file = input("Укажите файл для сжатого текста:\n")
if check(comp_file):
    comp_text = write(comp_file, encoded_text)
else:
    print("Файла не существует или указан неверный путь")

file_to_decode = input("Укажите файл с сжатым текстом:\n")
if check(file_to_decode):
    print(f"Сжатый текст:\n{read(file_to_decode)}")
    decoded_text = decode(read(file_to_decode))
    print(f"Восстановленный текст:\n{decoded_text}")
else:
    print("Файла не существует или указан неверный путь")