import requests

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

try:
    result = requests.request('GET', url)

except Exception as e:
    print(e)
else:
    with open('aaa.txt', 'w+', encoding='utf-8') as file:

        counter = 0
        print(result.json()[1]['exchangedate'], file=file)
        for currency in result.json():
            counter += 1

            file.write(f'{counter}. {currency["txt"]} ({currency["cc"]}) to UAH: {currency["rate"]} \n')
