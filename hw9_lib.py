from random import randint
import time


def get_number_from_user(MSG):
    """
    Func to get number from user. Number must be in 1-100 range.
    Returns:
        (int)
    """
    while True:
        try:
            number = int(input(f'{MSG}Enter int (1-100): '))
        except:
            print('It\'s not int')
        else:
            if number < 1 or number > 100:
                continue
            return number


def get_random_number():
    """
    Random number from computer.
    Returns:
        (int)
    """
    flow = 1
    celling = 100

    random_number = randint(flow, celling)
    return random_number, flow, celling


def get_attempts_to_guess():
    """

    :return:
    (int)
    """

    attempts = get_number_from_user('Enter number of attempts\n')
    if attempts < 1:
        attempts = 1
    return attempts


def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    difference = abs(user_number - to_guess)
    if to_guess == user_number:
        return True
    else:
        if difference >= 10:
            print('Холодно')
        elif difference >= 5 and difference < 10:
            print('Тепло')
        if difference >= 1 and difference <= 4:
            print('Гаряче')

        return False


def timing_formating(func):
    """

    :param func:
    :return:
    (func)
    """
    def wrapper(*args, **kwargs):

        time_start = time.time()
        func(*args, **kwargs)

        time_end = time.time()
        print('Function worked', time_end - time_start, 'sec.')

    return wrapper

