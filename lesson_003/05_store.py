# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
item_quantity = 0
item_price = 0
# Объявление переменных для Столов
tables_quantity = 0
tables_price = 0
total_tables_price = 0
total_tables_quantity = 0

# Объявление переменных для Диванов
sofas_quantity = 0
sofas_price = 0
total_sofas_price = 0
total_sofas_quantity = 0

# Объявление переменных для Стульев
chair_quantity = 0
chair_price = 0
total_chairs_price = 0
total_chairs_quantity = 0

for codes in enumerate(goods.items()):
        item = codes[1][0]
        code = codes[1][1]
        print(item, code)

for items in store.items():
    if items[0] == '12345':
        lamp_item = items[1][0]
        lamp_quantity = int(lamp_item['quantity'])
        lamp_price = int(lamp_item['price'])
        print(f'Ламп - {lamp_quantity} шт, стоимость {lamp_quantity * lamp_price} руб')
    elif items[0] == '23456':
        for i in range(len(items)):
            table_item = items[1][i]
            tables_quantity = int(table_item['quantity'])
            tables_price = int(table_item['price'])
            total_tables_quantity += tables_quantity
            total_tables_price += tables_quantity * tables_price
        print(f'Столов - {total_tables_quantity} шт, стоимость {total_tables_price} руб')
    elif items[0] == '34567':
        for i in range(len(items)):
            sofa_item = items[1][i]
            sofas_quantity = int(sofa_item['quantity'])
            sofas_price = int(sofa_item['price'])
            total_sofas_quantity += sofas_quantity
            total_sofas_price += sofas_quantity * sofas_price
        print(f'Диванов - {total_sofas_quantity} шт, стоимость {total_sofas_price} руб')
    elif items[0] == '45678':
        for i in range(len(items)):
            chair_item = items[1][i]
            chairs_quantity = int(chair_item['quantity'])
            chairs_price = int(chair_item['price'])
            total_chairs_quantity += chairs_quantity
            total_chairs_price += chairs_quantity * chairs_price
        print(f'Стульев - {total_chairs_quantity} шт, стоимость {total_chairs_price} руб')
