
import requests
from pprint import pprint

"""
завантажити використовуючи requests структуру даних з

https://dummyjson.com/todos

та вивести на екран не виконані значення todo з тих даних, які до вас прийшли
"""

url = 'https://dummyjson.com/todos'
todos = requests.get(url)
todos_ready=todos.json()

for id in range(todos_ready['limit']):
    if not todos_ready['todos'][id]['completed']:
        print(todos_ready['todos'][id]['todo'])

