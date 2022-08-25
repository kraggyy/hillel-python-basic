import requests

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


def currency_rate():
    try:
        result = requests.request('GET', url)

    except Exception as e:
        print(e)
    else:
        if content := result.headers.get('Content-Type'):
            if content == 'application/json':
                if 300 > result.status_code >= 200:
                    with open('aaa.txt', 'w+', encoding='utf-8') as file:
                        counter = 0
                        head_date = (result.json()[1]['exchangedate']).get
                        print(head_date, file=file)
                        for currency in result.json():
                            counter += 1
                            txt = currency["txt"].get
                            cur_code = currency["cc"].get
                            rate = currency["rate"].get
                            file.write(f'{counter}. {txt} ({cur_code}) to UAH: {rate} \n')


if __name__ == '__main__':
    currency_rate()
