MSG_THS = 'Дякую!'
MSG_WARNING_ALPHA = 'Вводити потрібно тільки букви! Ввести можна тільки одне слово! Спробуйте ще раз!'
MSG_WARNING_INT = 'Вводити потрібно тільки додатні числа! Вводити можна число не більше числа букв в вашому слові! Спробуйте ще раз!'

while True:
    user_wrd_input = input("Введіть слово -->")
    if user_wrd_input.isalpha():
        print(MSG_THS)
        break
    else:
        print(MSG_WARNING_ALPHA)

while True:
    user_nmbr_input = input("Введіть число -->")
    if user_nmbr_input.isdigit():
        print(MSG_THS)
    user_nmbr_input = int(user_nmbr_input)
    if len(user_wrd_input) >= user_nmbr_input:
        break
    else:
        print(MSG_WARNING_INT)

user_symbol = user_wrd_input[user_nmbr_input - 1]
result = f"{user_nmbr_input} символ з слова {user_wrd_input} це {user_symbol}"
print(result)