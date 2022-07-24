"""
Напишіть функцію, що приймає два аргументи. Функція повинна
якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
у будь-якому іншому випадку повернути кортеж з цих аргументів
"""

def my_func(agr_1, arg_2):

    type_agr_1 = type(agr_1)
    type_agr_2 = type(arg_2)

    if (type_agr_1 in (int, float)) and (type_agr_2 in (int, float)):
        result = agr_1 * arg_2
    elif type_agr_1 == str and type_agr_2 == str:
        result = agr_1 + arg_2
    elif type_agr_1 == str:
        result = {agr_1: arg_2}
    else:
        result = agr_1, arg_2

    return result


# result = my_func(False, True)
# print(result)
result = my_func(1, 2.3)
print(result)
result = my_func('asdsd','asdasdasd')
print(result)
result = my_func('asddasd',23)
print(result)


