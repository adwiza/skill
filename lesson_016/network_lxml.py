import requests
import lxml.html

# Пробуем вытащить актуальное время по UTC

# 1. Получаем HTML документ
time_response = requests.get('https://www.utctime.net/')
# 2. Преобразуем его в дерево
html_tree = lxml.html.document_fromstring(time_response.text)
# 3. Вытаскиваем нудное по шаблону
list_of_matches = html_tree.xpath("//*[@id='time2']")
print(f'Время в UTC {list_of_matches[0].text}')

