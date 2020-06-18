# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(start_point, angle=90, length=100):
    """ Эта функция рисует фрактал.

    """

    first_branch = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
    first_branch.draw()
    first_next_point = first_branch.end_point
    first_next_angle = angle + sd.random_number(18, 32)

    second_branch = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
    second_branch.draw()
    second_next_point = second_branch.end_point
    second_next_angle = angle - sd.random_number(18, 32)

    length *= (sd.random_number(75, 90) / 100)

    if length < 10:
        return
    else:
        draw_branches(first_next_point, angle=first_next_angle, length=length)
        draw_branches(second_next_point, angle=second_next_angle, length=length)


zero_point = sd.get_point(500, 0)
zero_branch = sd.get_vector(zero_point, angle=90, length=100)
zero_branch.draw()
draw_branches(start_point=zero_branch.end_point)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


