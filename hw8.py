import file_for_hw8


def game():
    '''
    Funcion for figuring out who is the winner.
    :return:
    '''
    user_choice = file_for_hw8.user()
    computer_choice = file_for_hw8.computer()
    if computer_choice == user_choice:
        print('Draw')
        file_for_hw8.win_results['draw'] += 1
    elif file_for_hw8.WIN_RULES[computer_choice] == user_choice:
        file_for_hw8.win_results['loose'] += 1
        print('Loose')
    else:
        file_for_hw8.win_results['win'] += 1
        print('Win')

if __name__ == '__main__':
    game()
    game()
    game()
    print(file_for_hw8.win_results)
