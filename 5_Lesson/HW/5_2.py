# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(data: str):
    encoding = ""
    prev_char = ''
    count = 1

    if not data:
        return "Файл пустой"

    else:
        for char in data:
            if char != prev_char:
                if prev_char:
                    encoding += str(count) + prev_char
                count = 1
                prev_char = char
            else:
                count += 1
        encoding += str(count) + prev_char
        return encoding



def decode(data: str):
    count = ""
    decode = ""

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += int(count) * char
            count = ""
    return decode



def read(file: str):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def write(file: str, content: str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

text_to_encode = input("Укажите файл с текстом для сжатия:\n")
print(f"Исходный текст:\n{read(text_to_encode)}")
encoded_text = encode(read(text_to_encode))
print(f"Сжатый текст:\n{encoded_text}")
comp_text = write(input("Укажите файл для сжатого текста:\n"), encoded_text)

text_to_decode = input("Укажите файл с сжатым текстом:\n")
print(f"Сжатый текст:\n{read(text_to_decode)}")
decoded_text = decode(read(text_to_decode))
print(f"Восстановленный текст:\n{decoded_text}")