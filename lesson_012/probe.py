import os
from pprint import pprint

import pandas as pd

work_dir = 'trades'
list_of_files = os.listdir(work_dir)
lines = []
all_data = pd.DataFrame(columns=['Тикер', 'Минималная цена', 'Максимальная цена', 'Средняя цена', 'Волатильность'])
saved_data = []
for file in list_of_files:
    f = open(os.path.join(work_dir, file), "r")
    data_frame = pd.read_csv(f, index_col=None, usecols=['PRICE'])
    # FINDING MAX AND MIN

    for i in enumerate(list_of_files):
        max_price = data_frame['PRICE'].max().round(2)
        min_price = data_frame['PRICE'].min().round(2)
        average_price = ((max_price + min_price) / 2).round(2)
        volatility = (((max_price - min_price) / average_price) * 100).round(2)
        ticker = i[1]
        # all_data = [('Тикер ' + str(ticker[7:11]), min_price, max_price, average_price, volatility)]
        all_data = [('Тикер ' + str(ticker[7:11]), volatility)]
        saved_data.append(all_data)
        f.close()

zero_volatility = []
max_volatility = []
min_volatility = []
all_elems = []

# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12

for row in saved_data:
    for elem in row:
        if elem[1] == 0:
            zero_volatility.append(elem[0])
        else:
            all_elems.append(elem)


def get_key(item):
    return item[1]


all_elems.sort(key=get_key, reverse=False)

for row in all_elems[-3:]:
    for elem in row:
        max_volatility.append(elem)

all_elems.sort(key=get_key, reverse=True)

for row in all_elems[-3:]:
    for elem in row:
        min_volatility.append(elem)


print('Минимальная волатильность:\n', ''.join(str(min_volatility)))
print('Максимальная волатильность:\n', max_volatility)
print('Нулевая волатильность:\n', zero_volatility)
