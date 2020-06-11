#!/usr/bin/env python
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

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_cost2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
# или проще (/сложнее ?)
table_code = goods['Стол']
tables_item = store[table_code][0]
tables_item2 = store[table_code][1]
tables_quantity = tables_item['quantity']
tables_quantity2 = tables_item2['quantity']
table_price = tables_item['price']
table_price2 = tables_item2['price']
table_cost = (tables_quantity * table_price) + (tables_quantity2 * table_price2)
print('Стол1 -', tables_quantity, 'шт, стоимость', table_cost, 'руб')
print('Стол2 -', tables_quantity2, 'шт, стоимость', table_cost2, 'руб')

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
# или проще (/сложнее ?)
sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_quantity = sofas_item['quantity']
sofa_price = sofas_item['price']
sofa_cost = sofas_quantity * sofa_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
# или проще (/сложнее ?)
chair_code = goods['Стул']
sofas_item = store[chair_code][0]
chairs_quantity = tables_item['quantity']
table_price = tables_item['price']
table_cost = tables_quantity * table_price
print('Стул -', tables_quantity, 'шт, стоимость', table_cost, 'руб')
##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






