"""почему-то не работает"""
import requests
from bs4 import BeautifulSoup
import csv#импорт нужного
url = 'https://bankdabrabyt.by/currency_exchange/grodno/'#ссылка на курсы банка
r = requests.get(url)#Статус ответа если 200 то норма
print(r)
soup = BeautifulSoup(r.text,'html.parser')#Преобразование в дерево тегов
print(soup)# Просмотр дерева тегов
items = soup.find_all('tr')# Выборка данных из дерева тегов
# print(items)
items.pop(-1)
# print(items)
courses = []
for item in items:
    _item = item.find_all("td")
    courses.append({
        'naim': _item[0].get_text(),
        'curAmount': _item[2].get_text(),
        'curs': _item[3].get_text().strip()
    })
print(courses)
with open('curs.csv','w') as file:# Запись в csv-файл
    writer = csv.DictWriter(
        file,
        fieldnames = ['naim','curAmount','curs'],
        delimiter = ';',
        lineterminator = '\r',
        quoting = csv.QUOTE_MINIMAL
    )
    writer.writeheader();
    for elem in courses:
        writer.writerow(elem)