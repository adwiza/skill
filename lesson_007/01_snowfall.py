# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
sd.resolution = (1000, 700)

class Snowflake:
    length = 30
    n = 100

    def __init__(self):
        self.length = Snowflake.length
        self.n = Snowflake.n
        self.x = 50
        self.y = 700
        self.color = sd.COLOR_WHITE

    def move(self):
        while self.x <= 700:
            self.x += 10

    def draw(self):
        point = sd.get_point(self.x, self.y)
        draw_flake = sd.snowflake(center=point, color=self.color, length=self.length)
        self.y -= 100
        return draw_flake

    def can_fall(self):
        result = True
        if self.y <= -10:
            result = False
        return result

    def clear_previous_picture(self):
        return sd.clear_screen()

    def user_want_exit(self):
        pass

    def __str__(self):
        return f'Я снежинка длина луча {Snowflake.length}, цвет {self.color}'

flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
         break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
