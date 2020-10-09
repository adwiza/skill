# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
color = sd.COLOR_PURPLE


def get_polygon(n):

    def select_figure(*args, **kwargs):
        if n == 3:
            return triangle(*args, **kwargs)
        elif n == 4:
            result = square(*args, **kwargs)
            return result
        elif n == 5:
            result = pentagon(*args, **kwargs)
            return result
        elif n == 6:
            result = hexagon(*args, **kwargs)
            return result

    return select_figure


def triangle(point, angle=0, length=150):
    """ Эта функция
    рисует треугольник."""
    print('Рисуем треугольник')
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+120, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+240, length=length, width=3)
    v3.draw(color=color)


def square(point, angle=0, length=150):
    """ Эта функция рисует
    квадрат.
    """

    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length, width=3)
    v4.draw(color=color)


def pentagon(point, angle=0, length=150):
    """ Эта функция рисует
        пятиугольник.
        """

    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw(color=color)


def hexagon(point, angle=0, length=150):
    """ Эта функция рисует
    шестиугольник.
    """

    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=color)

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw(color=color)


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(200, 200), angle=13, length=100)

draw_pentagon = get_polygon(n=5)
draw_pentagon(point=sd.get_point(200, 200), angle=13, length=100)

draw_hexagon = get_polygon(n=6)
draw_hexagon(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
