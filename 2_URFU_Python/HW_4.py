import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.banki.ru/banks/ratings/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Таблица рейтинга банков
table = soup.find('tbody')

# Список для добавления данных
data = []

# Сбор данных
for row in table.find_all('tr'):
    cells = row.find_all('td')
    
    # Получаем значения из каждой ячейки
    rank = cells[0].text.strip()
    bank = cells[1].find('a').text.strip()
    index_december = cells[2].text.strip().replace(' ', '')
    index_november = cells[3].text.strip().replace(' ', '')
    change_in_money = cells[4].text.strip().replace(' ', '')
    change_in_percent = cells[5].text.strip().replace(' ', '')
    
    # Словарь с данными строки
    row_data = {
        'Место': rank,
        'Название банка': bank,
        'Показатель декабрь': index_december,
        'Показатель ноябрь': index_november,
        'Изменение в тыс.руб.': change_in_money,
        'Изменение в %': change_in_percent
    }
    
    # Добавляем словарь в список
    data.append(row_data)

# Создаем DataFrame из списка данных
df = pd.DataFrame(data)

pd.set_option('display.max_columns', None)  # Показать все столбцы
pd.set_option('display.expand_frame_repr', False)  # Не сокращать вывод по ширине экрана

# Вывод данных
print(df)