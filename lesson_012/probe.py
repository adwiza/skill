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
        max_price = data_frame['PRICE'].max()
        min_price = data_frame['PRICE'].min()
        average_price = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / average_price) * 100
        ticker = i[1]
        all_data = [(ticker[7:11], min_price, max_price, average_price, volatility)]
        saved_data.append(all_data)
        # saved_data = ({'Тикер': ticker[7:11], 'Минималная цена': min_price, 'Максимальная цена': max_price,
        #                'Средняя цена': average_price,
        #                'Волатильность': volatility})
        # # saved_data = pd.DataFrame(columns=['Тикер', 'Минималная цена', 'Максимальная цена', 'Средняя цена',
        #                                    'Волатильность'])
        # saved_data.append({'Тикер': ticker[7:11]}, ignore_index=True)
        # print(saved_data)
        # print(f'Тикер {ticker[7:11]}')
        # print(f'Минималная цена {min_price}')
        # print(f'Максимальная цена {max_price}')
        # print(f'Средняя цена: {average_price} Волатильность:  {volatility:.2f}%')

        f.close()
pprint(saved_data)
