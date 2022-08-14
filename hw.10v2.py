"критерієм перевірки буде проходження всіх ассертів"

##############################################################################
############                                                     #############
############                      TASK 1                         #############
############                                                     #############
##############################################################################
"""
написати декоратор wrap_validate, який не приймає жодних параметрів
його задача - перевірити, що функція, яку він задекорував, обовязково отримала
в своїх аргументах параметр 'password' (згадуємо про * в написанні аргументів функції)
значення 'password' повинне бути стрічкою, довжиною не менше 10 символів,
та містити в собі латинські літери (регістр не принципово), арабські цифри та знак '!"

кожну з перевірок отриманого значення паролю виконуємо в ОКРЕМІЙ функції, функції робимо
універсальними, називаємо їх (з опційними параметрами)
- is_valid_length(length=10)
- has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm') (це приклад для латинських букв, повертає тру, якщо хоч
один символ в стрічці, аналогічно зробити для цифр та знаку оклику (у вас буде 3 виклики функції в середині декоратора
з різними параметрами)
- is_string()

якщо  'password'  відсутній - викликаємо помилку
raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

якщо  'password'  не задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': False,
}

якщо  'password'  задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': True,
}

зауважте, що str(func(*args, **kwargs)) МАЄ бути довжиною не більше 100 символів
якщо даний результат буде довшим за 100 символів, то стрічка має бути обрізана до 100 символів, причому останні
три символи мають бути ... (трьома крапками)
тут ви вже й самы здогадалися написати функцію на виконання даної роботи (тут вже без підказок)
"""


def out_max_length(string, length=100):
    if len(string) <= length:
        return string
    else:
        return string[:length - 3] + '...'


def has_any_symbols(string, symbols):
    '''
    func gets str
    :param string:
    :param symbols:
    :return: bool
    '''
    for letter in string.lower():
        if letter in symbols:
            return True
    return False


def is_string(string):
    '''
    func gets any type
    :param string:
    :return: bool
    '''
    if type(string) == str:
        return True
    return False


def is_valid_length(string, length=10):
    """
    disignided for str but to provide crushing makes str
    :param string:
    :param length:
    :return: bool
    """
    string = str(string)
    if len(string) <= length:
        return True
    return False


def wrap_validate(func):
    def wrapper(*args, **kwargs):

        if not 'password' in kwargs:
            raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

        val1 = has_any_symbols(kwargs['password'], "qwertyuiopasdfghjklzxcvbnm")
        val2 = has_any_symbols(kwargs['password'], "1234567890")
        val3 = has_any_symbols(kwargs['password'], "!")
        val4 = is_string(kwargs['password'])
        val5 = is_valid_length(kwargs['password'])

        if val1 and val2 and val3 and val4 and val5:
            return {'result': out_max_length(str(func(*args, **kwargs))),
                    'is_secure': True,
                    }

        return {'result': out_max_length(str(func(*args, **kwargs))),
                'is_secure': False,
                }

    return wrapper


##############################################################################
############                                                     #############
############                      TASK 2                         #############
############                                                     #############
##############################################################################
"""
написати функцію registration, яка приймає
- позиційний аргумент id, стрічка або число - не важливо,  значення за замовчуванням - відсутнє
- позиційний або іменований аргумент login, тип даних - не важливий, значення за замовчуванням - відсутнє
- позиційний або іменований аргумент notes, тип даних - не важливий, значення за замовчуванням - відсутнє
- password - тип даних - не важливий, значення за замовчуванням - відсутнє

в середині функції вставити код (зназок для отримання даних прописаний нижче)
date = datetime.date.today()

результат робити функції - стрічка
f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

задекоруйте написаним в завданні 1 декоратором
"""
import datetime


@wrap_validate
def registration(id, login, notes, password):
    date = datetime.date.today()

    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

print(registration(14, 'qwe', 'sdfgsdfg', password='sdfggs'))

##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)
в цій умові створіть assert на всі створені функції (окрім декоратора), викликайте функції з різними параметрами 
(довжина слів, різні текстовки....)
на кожну функцію, що використовується в декораторі, має бути мінімум 3 ассерта,

функцію registration перевіряйте з огляду на роботу декоратора (ключі, значення). обовязково перевірте кількість ключів, 
тип даних в значеннях, назви ключів, значення отриманого результату в залежності від переданих даних   

ВАЖЛИВО 
функцію registration ассертимо ТІЛЬКИ при передачі їй валідних даних (поля паролю)
"""
if __name__ == '__main__':
    assert out_max_length('*' * 100) == '*' * 100
    assert out_max_length('*' * 50) == '*' * 50
    assert out_max_length('*' * 120) == '*' * 97 + '...'

    assert (has_any_symbols("qwertyuiopasdfsfhafgkgfsghjklzxcvbnm", 'qwertyuiopasdfghjklzxcvbnm'))
    assert (has_any_symbols("qwertyuiopa0456sdfghjklzxcvbnm", '0123456789'))
    assert (has_any_symbols("qwertyuiop!!!!!!!!!asdfghjklzxcvbnm", '!'))

    assert is_string('asdfasdf')
    assert is_string('asdfasdf123123123123!')
    assert is_string(93761951) == False

    assert is_valid_length('asdasfhghdjfhg;sdfg;sdhfg;lksdfg') == False
    assert is_valid_length('asd')
    assert is_valid_length(5135115)

    assert registration(14, 'qwe', 'sdfgsdfg', password='asdhfgadsfjashdflsdhfljashdfh32143745697342374y09!') == {
        'result': 'User qwe created account on 2022-08-14 with password "asdhfgadsfjashdflsdhfljashdfh32143745697342...',
        'is_secure': False}
    assert type(
        registration(14, 'qwe', 'sdfgsdfg', password='asdhfgadsfjashdflsdhfljashdfh32143745697342374y09!')) == dict
    assert registration(14, 'qwe', 'sdfgsdfg', password='sdfggs') == {
        'result': 'User qwe created account on 2022-08-14 with password "sdfggs". Additional information: sdfgsdfg',
        'is_secure': False}

##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################

'Как остановить драку слепых?'
'Крикнуть: я ставлю на того с ножом'
