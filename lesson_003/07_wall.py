# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

import simple_draw as sd

width = 100
height = 50
y = 0
y1 = height
for i in range(12):
    start_point = sd.get_point(0, y)
    end_point = sd.get_point(600, y)
    sd.line(start_point, end_point, sd.COLOR_ORANGE, width=3)
    if i % 2 == 0:
        x1 = 0
        x2 = 0
        for _ in range(7):
            start_point = sd.get_point(x1, y)
            end_point = sd.get_point(x2, y + y1)
            sd.line(start_point, end_point, sd.COLOR_ORANGE, width=3)
            x1 += width
            x2 += width
    else:
        x1 = width/2
        x2 = width/2
        for _ in range(6):
            start_point = sd.get_point(x1, y)
            end_point = sd.get_point(x2, y + y1)
            sd.line(start_point, end_point, sd.COLOR_ORANGE, width=3)
            x1 += width
            x2 += width
    y += height

sd.pause()
