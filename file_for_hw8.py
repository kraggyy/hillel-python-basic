import random


WIN_RULES = {
    'камень': "ножницы",
    "ножницы": "бумага",
    'бyмага': "камень",
}

win_results = {
    'win': 0,
    'loose': 0,
    'draw': 0,
}


def computer():
    """
    Function to get random choosen word from computer for game process
    :return:
    """

    comp_choice = random.choice(list(WIN_RULES))

    return comp_choice


def user():
    """
    Function to get number from user, for convert it in some key from WIN_RULES
    :return:
    """

    while True:
        user_input = input('Введите данные {1=камень, 2=ножницы, 3=бумага} -->').strip()
        if user_input in ['1', '2', '3']:
            user_input = int(user_input)
            user_choice = list(WIN_RULES)[user_input - 1]
            return user_choice
        else:
            print('Введите нужное значение!')
            continue







