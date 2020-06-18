# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def figure_select():
    """ Эта функция выбора фигуры.
    """
    print('Выберите фигуру:')
    print('0: Треугольник')
    print('1: Квадрат')
    print('2: Пятиугольник')
    print('3: Шестиугольник')

    while True:
        try:
            user_select = int(input('Выберите фигуру? '))
        except ValueError:
            print('Номер фигуры должен быть числом!')
        else:
            if user_select not in range(4):
                print('Выберите число от 0 до 3')
            else:
                break

    if user_select == 0:
        return triangle()
    elif user_select == 1:
        return square()
    elif user_select == 2:
        return pentagon()
    else:
        return hexagon()


def triangle():
    """ Эта функция
    рисует треугольник.
    """

    length = 200
    x = 200
    y = 200
    angle = 30
    point0 = sd.get_point(x, y)

    v1 = sd.get_vector(start_point=point0, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=color)


def square():
    """ Эта функция рисует
    квадрат.
    """
    length = 200
    x = 200
    y = 200
    angle = 30
    point0 = sd.get_point(x, y)

    v1 = sd.get_vector(start_point=point0, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length, width=3)
    v4.draw(color=color)


def hexagon():
    """ Эта функция рисует
    шестиугольник.
    """
    length = 200
    x = 200
    y = 200
    angle = 0
    point0 = sd.get_point(x, y)

    v1 = sd.get_vector(start_point=point0, angle=angle, length=length, width=3)
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


def pentagon():
    """ Эта функция рисует
        пятиугольник.
        """
    length = 200
    x = 200
    y = 200
    angle = 30
    point0 = sd.get_point(x, y)

    v1 = sd.get_vector(start_point=point0, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw(color=color)


color = sd.COLOR_PURPLE

figure_select()

sd.pause()
