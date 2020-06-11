#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}


moscow = sites['Moscow']
x_moscow = moscow[0]
y_moscow = moscow[1]

london = sites['London']
x_london = london[0]
y_london = london[1]

paris = sites['Paris']
x_paris = paris[0]
y_paris = paris[1]

# Считаем расстояние между городами

# Москва - Лондон
moscow_london = ((x_moscow - x_london) ** 2 + (y_moscow - y_london) ** 2) ** 0.5
london_moscow = moscow_london

# Москва - Париж
moscow_paris = ((x_moscow - x_paris) ** 2 + (y_moscow - y_paris) ** 2) ** 0.5
paris_moscow = moscow_paris

# Лондон - Париж
london_paris = ((x_london - x_paris) ** 2 + (y_london - y_paris) ** 2) ** 0.5
paris_london = london_paris

# Создание пустых словарей для заполнения
distances['Moscow'] = {}
distances['Paris'] = {}
distances['London'] = {}

distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London']['Paris'] = london_paris
distances['Paris']['London'] = paris_london

distances['Paris']['Moscow'] = paris_moscow
distances['Paris']['London'] = paris_london

print(distances)
print(distances['Moscow']['Paris'])



