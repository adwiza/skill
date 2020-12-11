# -*- coding: utf-8 -*-

#
# 15.06 Практика
#

# Задача: подсчитать выплату суточных агенту 007.
#
# Дано: файл с зашифрованными посланиями, в которых содержатся информация о датах, городах и потраченных суммах:
# external_data/Bond.json
#
# Шифр следующий:
# в каждом послании среди случайных символов содержатся:
# - дата в формате "jbdDDMMYY"
# - город в формате "jbcCITYNAMEjbc"
# - сумма потраченных за день денег в местной валюте в формате "jbeFLOATjbe"
#
# Требуется: составить два файла с тратами по дням, и по месяцам для бухгалтерии МИ-6.
import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN
from pprint import pprint

re_data = r'jbd(\d{6})'
re_city = r'jbc(\w+)jbc'
re_expenses = r'jbe(\d+\.\d+)jbe'

with open('python_snippets/external_data/Bond.json', 'r') as json_file:
    data = json.load(json_file)

pprint(data)
print(len(data))

# Создаем функции форматирования

dates = set()
cities = set()
for key, message in data.items():
    dates.add(re.search(re_data, message)[1])
    cities.add(re.search(re_city, message)[1])

exchanges = {
    'токио': Decimal(0.007),  # Japan Yena -> Pounds
    'берлин': Decimal(0.87),  # Euro -> Pounds
    'лондон': Decimal(1.0),  # Pounds -> Pounds
    'москва': Decimal(0.12),  # Roubles -> Pounds
}


def date_time_to_str(date_str):
    return datetime.strptime(date_str, '%d%m%y')


def expenses_str_to_decimal(expenses_str, city):
    return Decimal(expenses_str) * exchanges[city]


# Создаем результирующий массив

result = []
for key, message in data.items():
    date_str = re.search(re_data, message)[1]
    city = re.search(re_city, message)[1]
    expenses_str = re.search(re_expenses, message)[1]

    result.append({
        'date': date_time_to_str(date_str),
        'city': city,
        'expenses': expenses_str_to_decimal(expenses_str, city),
    })

pprint(result)

result_sorted = sorted(result, key=lambda record: ['date'])

# Генерируем подробный файл

result_formated = [
    {
        'date': record['date'].strftime('%d.%m.%Y'),
        'city': record['city'],
        'expenses': str(record['expenses'].quantize(Decimal('1.00'), ROUND_HALF_EVEN)),
    }
    for record in result_sorted

]

pprint(result_formated)

with open('python_snippets/external_data/Bond_MY_Detail.csv', 'w') as out_detail_file:
    writer = csv.DictWriter(out_detail_file, fieldnames=['date', 'city', 'expenses'])
    writer.writeheader()
    writer.writerows(result_formated)

# Аггрегируем по месяцам
result_aggregated_temp = defaultdict(lambda: {'cities': set(), 'expenses_sum': Decimal(0),
                                              'month': '', 'date_for_sort': None})
for record in result_sorted:
    month_datetime = datetime(year=record['date'].year, month=record['date'].month, day=1)
    month = month_datetime.strftime('%m.%Y')
    result_aggregated_temp[month]['cities'].add(record['city'])
    result_aggregated_temp[month]['expenses_sum'] += record['expenses']
    result_aggregated_temp[month]['month'] = month
    result_aggregated_temp[month]['date_for_sort'] = month_datetime


pprint(result_aggregated_temp)

result_aggregated = sorted(result_aggregated_temp.values(), key=lambda record: record['date_for_sort'])

result_aggregated_formated = [
    {
        'month': record['month'],
        'cities': ', '.join(record['cities']),
        'expenses_sum': str(record['expenses_sum'].quantize(Decimal('1.00'), ROUND_HALF_EVEN)),
    }
    for record in result_aggregated

]

pprint(result_aggregated_formated)

with open('BondDetailByMonth.csv', 'w') as out_detail_file:
    writer = csv.DictWriter(out_detail_file, fieldnames=['month', 'cities', 'expenses_sum'])
    writer.writeheader()
    writer.writerows(result_aggregated_formated)
