"""
Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент,
перетворений на float.
Якщо перетворити не вдається функція має повернути 0.
"""
def my_func(arg):
    try:
        result = float(arg)
    except:
        result = 0
    return result


user_input = input('Введіть ваш аргумент --> ')
result = my_func(user_input)
print(result)