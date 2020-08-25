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

# TODO здесь ваш код
import zipfile


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
            if self.sequence in self.stat:
                if char in self.stat[self.sequence]:
                    self.stat[self.sequence][char] += 1
                else:
                    self.stat[self.sequence][char] = 1
            else:
                self.stat[self.sequence] = {char: 1}
            self.sequence = self.sequence[1:] + char


collector = CharCollector(file_name='voyna-i-mir.txt.zip')
collector.collect()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
