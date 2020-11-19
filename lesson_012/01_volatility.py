# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
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
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле
import operator
import zipfile
import csv
import os.path
from collections import defaultdict
from multiprocessing import Process
from pprint import pprint
from threading import Thread

import numpy as np
import pandas as pd
from operator import itemgetter, attrgetter, methodcaller

from IPython.core.display import display

work_dir = 'trades'
list_of_files = os.listdir(work_dir)
lines = []


class VolatilityCalculator:

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.result = defaultdict(int)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for file_name in zfile.namelist():
            zfile.extract(file_name)

    def run(self):
        self.result = defaultdict(int)
        self.zv = defaultdict(int)
        self.result_data_max = 0
        self.result_data_min = 0
        with open(os.path.join(work_dir, self.file_name)) as f:
            data_frame = pd.read_csv(f, index_col=None, usecols=['PRICE'])
            # FINDING MAX AND MIN
            max_price = data_frame['PRICE'].max()
            min_price = data_frame['PRICE'].min()
            average_price = (max_price + min_price) / 2
            volatility = ((max_price - min_price) / average_price) * 100
            if volatility == 0:
                self.zv = [str(self.file_name[7:11]), volatility]
                # print('Нулевая волатильность', self.zv)
            else:
                data_file = 'data.csv'
                result_data_max = []
                result_data_min = []
                all_data = pd.DataFrame([(str(self.file_name[7:11]), volatility)])
                if os.path.exists(data_file):
                    with open(data_file) as fff:
                        saved_data = pd.read_csv(fff, names=['ticker', 'volatility'])
                        self.result_data_max += saved_data['volatility'].max()
                        self.result_data_min += saved_data['volatility'].min()
                        my_dict_max = dict(ticker=self.file_name[7:11], vol=self.result_data_max)
                        my_dict_min = dict(ticker=self.file_name[7:11], vol=self.result_data_min)
                # result_data = [saved_data['ticker'], saved_data['volatility'].min()]
                print(my_dict_max)
                print(my_dict_min)
            # print(self.result_data_min)


def main():
    payloads = [VolatilityCalculator(file_name=file) for file in list_of_files]
    for payload in payloads:
        payload.run()


if __name__ == '__main__':
    main()
