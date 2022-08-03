import hw9_lib


@hw9_lib.timing_formating
def game():
    number_to_guess, flow, celling = hw9_lib.get_random_number()
    attempts_left = hw9_lib.get_attempts_to_guess()

    print(f"You need to guess from {flow} to {celling}. ")

    while attempts_left > 0:
        user_number = hw9_lib.get_number_from_user('Enter your guess number: ')
        if hw9_lib.check_numbers(number_to_guess, user_number):
            print('You WIN!!!!')
            break
        attempts_left -= 1


if __name__ == "__main__":
    print(game())
