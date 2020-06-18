# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом
sd.resolution = (1200, 800)
# sd.background_color = sd.COLOR_WHITE

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def color_select():
    """ Эта функция выбора цвета
    для фигуры.
    """
    # Досупные цвета
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    print('Выберите цвет:')
    print('0: Красный')
    print('1: Оранжевый')
    print('2: Желтый')
    print('3: Зеленый')
    print('4: Сине-зелёный')
    print('5: Голубой')
    print('6: Лиловый')

    while True:
        try:
            user_color = int(input('Введите желаемый цвет? '))
        except ValueError:
            print('Извините, цвет должен  быть числом!')
        else:
            if user_color not in range(7):
                print('Выберите число от 0 до 6')
            else:
                break

    return rainbow_colors[user_color]


def triangle():
    """ Эта функция
    рисует треугольник.
    """

    length = 150
    x = 100
    y = 50
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
    length = 150
    x = 900
    y = 50
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
    length = 150
    x = 900
    y = 500
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
    length = 150
    x = 150
    y = 500
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


color = color_select()
square()
triangle()
hexagon()
pentagon()

sd.pause()
