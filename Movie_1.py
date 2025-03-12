import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Lists_of_films'

response = requests.get(URL)
data = BeautifulSoup(response.text, 'html.parser')

categories = {}

# Находим раздел с категориями
for item in data.select('ul li'):
    if item.a:  # Проверяем, что элемент a существует
        link = item.a['href']
        name = item.a.get('title')  # Здесь получаем название категории

        if name and link:  # Проверяем, что оба значения существуют
            full_link = 'https://en.wikipedia.org' + link
            categories[name] = full_link

# Печатаем результат
for name, link in categories.items():
    print(name, '-----', link)

# Сохранение в файл
with open('Word_f.txt', 'w') as file:
    for name, link in categories.items():
        file.write(f"{name} - {link}\n")
