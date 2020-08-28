# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
# -*- encoding: utf-8 -*-
from __future__ import annotations

import re
from datetime import datetime
from pprint import pprint


class Event:

    def __init__(self, dt: datetime, rt: str):
        self.dt, self.rt = dt, rt

    @classmethod
    def from_string(self, string: str, pattern: str) -> Event:
        match = re.fullmatch(pattern, string)
        self.dt = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S.%f")
        self.rt = match.group(2)
        return Event(self.dt, self.rt)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Event(datetime={self.dt}, result={self.rt})"


class LogParser:

    def __init__(self, fileName: str):
        self.fileName = fileName
        self.events = []

    def read(self, pattern: str):
        with open(self.fileName, "rt") as file:
            lines = file.read().split("\n")
        self.events = [Event.from_string(line, pattern) for line in lines if line]

    @property
    def group_in_minutes(self) -> tuple:
        group_events = [[self.events[0]], ]
        for event in self.events[1:]:
            if (event.dt - group_events[-1][0].dt).seconds < 60:
                group_events[-1].append(event)
            else:
                group_events.append([event])
        return group_events


lg = LogParser("events.txt")
lg.read(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] (\w{2,3})")
pprint(lg.events)
pprint(lg.group_in_minutes)
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

