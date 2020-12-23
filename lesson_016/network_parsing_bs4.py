import requests
from bs4 import BeautifulSoup as soup
from html.parser import HTMLParser

response = requests.get('https://yandex.ru/')


# Просмотреть весь документ мы сможем командой
# print(response.text)


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Encountered a start tag: <{tag}>')

    def handle_endtag(self, tag):
        print(f'Encountered a end tag: </{tag}>')

    def handle_data(self, data):
        print(f'Encountered a some data: <{data.strip()}>')


# Для примера скормим нашщему парсеру пару строк
# parser = MyHTMLParser()
# parser.feed('''
# <html>
#     <head>
#         <title>Test</title>
#     </head>
#     <body>
#         <h1>Parse me!</h1>
#     </body>
# </html>
# ''')

# <a class="home-link home-link_black_yes inline-stocks__link" href="https://yandex.ru/news/quotes/2002.html"
# target="_blank" rel="noopener" data-statlog="news_rates_manual.id2002" data-statlog-showed="1">USD</a>

if response.status_code == 200:
    html_doc = soup(response.text, features='html.parser')
    list_of_values = html_doc.find_all('span', {'class': 'inline-stocks__value_inner'})
    list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)
