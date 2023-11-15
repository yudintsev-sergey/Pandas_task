'''
https://correlatesofwar.org/data-sets/
Проект "Correlates of War" - академическjt исследование истории войн.
Начат в 1963 году в Мичиганском университете политологом Дж. Дэвидом Сингером.
Занимаясь сбором данных об истории войн и конфликтов между государствами,
Сингер развил количественные исследования причин войн.

Статистику данного проекта я использовал с целью освоения пакета Pandas.
Ситуацию смоделировал несколько игровую. Все страны разбил на несколько кластеров и проиллюстрировал
известное утверждение о том, что в Крымской войне 1853-1854 года Россия проиграла в связи с тем, что
экономическая мощь объединившейся Европы была значительно выше.

Обозначения статистических показателей:
irst, Iron and steel production (thousands of tons)
milex, military Expenditures (For 1816-1913: thousands of current year British Pounds. For 1914+: thousands of current year US Dollars.)
milper, Military Personnel (thousands)
energy, Energy consumption (thousands of coal-ton equivalents)
pop, Total Population (thousands)
upop, Urban population (population living in cities with population greater than 100,000; in thousands)
cinc, Composite Index of National Capability (CINC) score
version, Version number of the data set
'''

import pandas as pd
import os.path
import matplotlib.pyplot as plt

COW_CODE = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'cow_codes.csv')
print(COW_CODE)
COW_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'nmc.csv')
print(COW_PATH)

n_in = int(input('Введите год начала анализа: '))
n_out = int(input('Введите год окончания анализа: '))

# Удаляем дубль-строки в файле с кодами
coding_data = pd.read_csv(COW_CODE, sep=',', header=0)
index_for_del = coding_data[coding_data.duplicated(keep='last')].index
coding_data_drop = coding_data.drop(index_for_del, inplace=True)

# Фантазийные блоки - Россия+, Саурон (США), Кольцо Саурона (Европа)
b = ['RUS', 'Sauron', 'Sring']
# ============================================
# Производство стали
steel = []
for i in range(3):
    bands = coding_data[coding_data['Block'] == b[i]]['StateAbb']
    cow_data = pd.read_csv(COW_PATH, sep=',', header=0)
    t_until_cw = cow_data[(cow_data['year'] > n_in) & (cow_data['year'] < n_out)]
    steel.append(t_until_cw[t_until_cw['StateNme'].isin(bands)]['irst'].sum())

labels = ['Россия+', 'США', 'Европа+']
fig, ax = plt.subplots()
ax.pie(steel, labels=labels, autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=1.0)
ax.set_title("Выплавка стали")
plt.show()

# ============================================
# Военный бюджет
milex = []
for i in range(3):
    bands = coding_data[coding_data['Block'] == b[i]]['StateAbb']
    cow_data = pd.read_csv(COW_PATH, sep=',', header=0)
    t_until_cw = cow_data[(cow_data['year'] > n_in) & (cow_data['year'] < n_out)]
    milex.append(t_until_cw[t_until_cw['StateNme'].isin(bands)]['milex'].sum())

labels = ['Россия+', 'США', 'Европа+']
fig, ax = plt.subplots()
ax.pie(milex, labels=labels, autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=1.0)
ax.set_title("Военный бюджет")
plt.show()

# ============================================
# Мобилизационный потенциал
milper = []
for i in range(3):
    bands = coding_data[coding_data['Block'] == b[i]]['StateAbb']
    cow_data = pd.read_csv(COW_PATH, sep=',', header=0)
    t_until_cw = cow_data[(cow_data['year'] > n_in) & (cow_data['year'] < n_out)]
    milper.append(t_until_cw[t_until_cw['StateNme'].isin(bands)]['milper'].sum())

labels = ['Россия+', 'США', 'Европа+']
fig, ax = plt.subplots()
ax.pie(milper, labels=labels, autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=1.0)
ax.set_title("Мобилизационный потенциал")
plt.show()
