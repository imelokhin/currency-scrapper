import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

# Получаем HTML с сайта курсов валют
url = "https://www.x-rates.com/table/?from=USD&amount=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Находим таблицу с курсами
table = soup.find("table", class_="tablesorter ratesTable")
rows = table.find_all("tr")[1:]

# Создаём Excel-файл
wb = Workbook()
ws = wb.active
ws.title = "Exchange Rates"

# Добавляем текущую дату и время
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ws.append(["Exchange rates as of", now])
ws.append([])  # пустая строка

# Заголовки таблицы
ws.append(["Currency", "Rate"])

# Заполняем таблицу
for row in rows:
    cols = row.find_all("td")
    currency = cols[0].text
    rate = cols[1].text
    ws.append([currency, rate])

# Сохраняем Excel-файл
wb.save("exchange_rates.xlsx")
print("✅ Saved to exchange_rates.xlsx")