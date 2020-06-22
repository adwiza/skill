# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

import simple_draw as sd

brick_x, brick_y = 100, 50

row = 0
for y in range(0, sd.resolution[1], brick_y):
    row += 1
    for x in range(0, sd.resolution[0], brick_x):
        x0 = x if row % 2 else x + brick_x // 2
        left_bottom = sd.get_point(x0, y)
        right_top = sd.get_point(x0 + brick_x, y + brick_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
sd.pause()
