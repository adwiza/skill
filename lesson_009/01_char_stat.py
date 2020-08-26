# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
from operator import itemgetter


class CharCollector:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.sequence = ' '
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if self.sequence in self.stat:
                    if char in self.stat[self.sequence]:
                        self.stat[self.sequence][char] += 1
                    else:
                        self.stat[self.sequence][char] = 1
                else:
                    self.stat[self.sequence] = {char: 1}
        return self.stat

    def output_with_sort(self):
        all_stats = collector.stat[' ']
        sorted_items = sorted(all_stats.items(), key=itemgetter(1), reverse=True)
        total = 0
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for char, stats in sorted_items:
            print(f'| {char:^8}|{stats:^10}|')
            print('----------+-----------')
            total += stats

        print(f'|  Итого  | {total}  |')
        print('+---------+----------+')


collector = CharCollector(file_name='voyna-i-mir.txt.zip')
collector.collect()
collector.output_with_sort()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
