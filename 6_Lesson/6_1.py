# Напишите программу
# вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *.
# Приоритет операций стандартный.
# Добавьте скобки, приоритет операций меняется.

actions = {
	    "^": lambda x, y: str(float(x) ** float(y)),
	    "*": lambda x, y: str(float(x) * float(y)),
	    "/": lambda x, y: str(float(x) / float(y)),
	    "+": lambda x, y: str(float(x) + float(y)),
	    "-": lambda x, y: str(float(x) - float(y))
	    }

operations = "8 + 2 * 4 + ( 6 + ( 2 - 3 * 7 + ( 77 - 11 ) ) * 2 )"

def prior(numbers: list):
    new_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] == '(':
            if '(' in numbers[i + 1:]:
                numbers = numbers[:i + 1] + prior(numbers[i + 1:])
            o = numbers.index(')', i)
            new_numbers.append(numbers[i + 1: o])
            i = o
        else:
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers

def calc(numbers: list):
    for i, num in enumerate(numbers):
        if isinstance(num, list):
            numbers[i] = calc(num)
    new_list = [i for i, sym in enumerate(numbers) if sym in "*/"]
    while new_list:
        j = new_list[0]
        a, b, c = numbers[j - 1: j + 2]
        numbers.insert(j - 1, actions[b](a, c))
        del numbers[j: j + 3]
        new_list = [i for i, sym in enumerate(numbers) if sym in "*/"]
    while len(numbers) > 1:
        a, b, c = numbers[: 3]
        del numbers[: 3]
        numbers.insert(0, actions[b](a, c))
    return numbers[0]

changed_list = prior(operations.split())
print(changed_list)
print(calc(changed_list))