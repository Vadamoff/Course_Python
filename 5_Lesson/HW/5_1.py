# Напишите программу,
# удаляющую из текста все слова,
# содержащие "абв".
# В тексте используется разделитель пробел.

from random import sample

def create_word_string(count: int):
    new_str = ""
    letters = "абв"
    for _ in range(count - 1):
        symbol = sample(letters, k = 3)
        new_str += "".join(symbol) + " "
    new_str += "".join(symbol)
    return new_str

# Вариант

# def create_word_string(count: int, chars: str = "абв", len: int = 3):
#     return " ".join("".join(sample(chars, len)) for _ in range(count))

def remove_word(str_in: str):
    new_str = str_in.replace("абв", "")
    return new_str.replace("  ", " ").strip()

# Вариант

# def simple_sentence(words: str) -> str:
#     return " ".join(words.replace("абв", "").split())

# Ещё вариант

# def simple_sentence(words: str) -> str:
#     return " ".join(i for i in words.split() if i != "абв")

text = create_word_string(int(input("Задайте количество слов в тексте:\n")))
print(f"Список слов:\n{text}")
print(f"Список после удаления 'абв':\n{remove_word(text)}")