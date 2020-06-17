# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x_start = 50
y_start = 50
step = 5
x_end = 500
y_end = 500

for color in rainbow_colors:
    line_color = color
    start_point = sd.get_point(x_start, y_start)
    end_point = sd.get_point(x_end, y_end)
    sd.line(start_point=start_point, end_point=end_point, color=line_color, width=4)
    x_start += 5
    x_end += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
radius = 300
step = 10
x_start = 300
y_start = 0
for color in rainbow_colors:
    circle_color = color
    radius += step
    center_point = sd.get_point(x_start, y_start)
    sd.circle(center_position=center_point, radius=radius, color=circle_color, width=20)
    y_start += 10
sd.pause()
