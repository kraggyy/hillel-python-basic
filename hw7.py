"""
Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
Наприклад :
"Тобі ж 5 років! Де твої батьки?"
"Вам 81 рік? Покажіть пенсійне посвідчення!"
"О, вам 33 роки! Який цікавий вік!"
Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.

"""
max_age = 120
MSG_INPUT_AGE_ALLOWED = f'\033[4;31m Вік необхідно ввести додатними числами! Максимально допустимий вік {max_age} років.\033[0m '
MSG_USER_INPUT = "\033[32mВведіть ваш вік ==>\033[0m "
MSG_NICE_AGE = "\033[30;43m О, вам {}! Який цікавий вік! \033[0m"
MSG_WHERE_PARENTS = "\033[1;31mТобі ж {}! Де твої батьки?\033[0m"
MSG_ACHTUNG = "\033[1;31mТобі лише {}, а це е фільм для дорослих!\033[0m"
MSG_DOCUMENTS = "\033[1;30;47mВам {}? Покажіть пенсійне посвідчення\033[0m"
MSG_NO_TICKETS = "\033[31mНезважаючи на те, що вам {}, білетів всеодно нема!\033[0m"

#ограничители

def limiter():
    while True:
        temp_age = input(MSG_USER_INPUT).lstrip('0')
        if temp_age.isdigit() and int(temp_age) <= max_age:
            str_age = temp_age
            numeric_age = int(str_age)
            return numeric_age
        print(MSG_INPUT_AGE_ALLOWED)



def age_counting(numeric_age):
    """
    Function for figuring out which MSG needs to be written, based on user`s age
    :param numeric_age:
    :return:
    """
    str_age = str(numeric_age)
    if len(str_age) > 1 and str_age.count(str_age[0]) == len(str_age):
        counting_result = (MSG_NICE_AGE)
    elif numeric_age < 7:
        counting_result = (MSG_WHERE_PARENTS)
    elif numeric_age < 16:
        counting_result = (MSG_ACHTUNG)
    elif numeric_age > 65:
        counting_result = (MSG_DOCUMENTS)
    else:
        counting_result = (MSG_NO_TICKETS)

    return counting_result


def word_changing(age):
    """
    Function for changing word form, based of user`s age
    :param age:
    :return:
    """
    age_str = str(age)
    if age >= 5 and age <= 20:
        word_result = age_str + ' років'
    elif age_str[-1] == '1':
        word_result = age_str + ' рік'
    elif age_str[-1] in {'234'}:
        word_result = age_str + ' роки'
    else:
        word_result = age_str + ' років'

    return word_result

def procesor():

    age = limiter()
    age_msg = age_counting(age)
    fresult = word_changing(age)
    return age_msg.format(fresult)
print(procesor())