# -*- coding: utf-8 -*-
import random

import numpy
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)
# sd.circle(center_position=point)
radius = 50
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
for _ in range(3):
    radius += 5
    # sd.circle(center_position=point, radius=radius, width=3)

# Нарисовать 10 пузырьков в ряд


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)

sd.pause()
