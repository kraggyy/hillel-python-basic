# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або функцію input()).
# - якщо користувачу менше 7 - вивести "Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр
# (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "А білетів вже немає!"


max_age = 120
MSG_INPUT_AGE_ALLOWED = f'\033[4;31m Вік необхідно ввести додатними числами! Максимально допустимий вік {max_age} років.\033[0m '
MSG_USER_INPUT = "\033[32mВведіть ваш вік ==>\033[0m "
MSG_NICE_AGE = "\033[30;43m Який цікавий вік! \033[0m"
MSG_WHERE_PARENTS = "\033[1;31mДе твої батьки?\033[0m"
MSG_ACHTUNG = "\033[1;31mЦе фільм для дорослих!\033[0m"
MSG_DOCUMENTS = "\033[1;30;47mПокажіть пенсійне посвідчення!\033[0m"
MSG_NO_TICKETS = "\033[31mА білетів вже немає!\033[0m"

#ограничители

while True:
    temp_age = input(MSG_USER_INPUT).lstrip('0')
    if temp_age.isdigit() and int(temp_age) <= max_age:
        str_age = temp_age
        numeric_age = int(str_age)
        break
    print(MSG_INPUT_AGE_ALLOWED)


if len(str_age) > 1 and str_age.count(str_age[0]) == len(str_age):
    print(MSG_NICE_AGE)
elif numeric_age < 7:
    print(MSG_WHERE_PARENTS)
elif numeric_age < 16:
    print(MSG_ACHTUNG)
elif numeric_age > 65:
    print(MSG_DOCUMENTS)
else:
    print(MSG_NO_TICKETS)
