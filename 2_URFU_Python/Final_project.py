import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data__1_.csv', encoding='cp1251', delimiter=';')

# Преобразовать тип данных в столбце ‘Дата создания’ при помощи метода pd.to_datetime
df['Дата создания'] = pd.to_datetime(df['Дата создания'], format='mixed')

# Добавить к данным два столбца: ‘Date’ и ’Hour’, взяв данные из столбца ‘Дата создания’
df['Date'] = df['Дата создания'].dt.date
df['Hour'] = df['Дата создания'].dt.hour

# Построить сводную таблицу, содержащую количество личных дел, принятых приёмной комиссией в течение каждого рабочего часа (index = 'Hour', columns = 'Date')
pivot_table = df.pivot_table(index='Hour', columns='Date', values='ЛД', aggfunc='count')

# Построить графическое представление данных в виде heatmap из библиотеки SeaBorn
plt.figure(figsize=(16, 6))
sns.heatmap(pivot_table, cmap='magma')
plt.title('Нагрузка на приёмную комиссию')
plt.xlabel('Дата')
plt.ylabel('Рабочий час')
plt.show()