# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):

        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0
        self.house = None

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}'

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def watch_MTV(self):
        cprint(f'{self.name} смотрел MTV целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 50
            cprint(f'{self.name} сходил в магазин за едой', color='magenta')
        else:
            cprint(f'{self.name} деньги кончились', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = randint(1, 6)

        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} заехал в дом!!!', color='cyan')

    def pick_up_a_cat(self, cat):
        cat.house = self.house
        cprint(f'Кот {cat.name} заехал в дом!!!', color='cyan')

    def cat_food_shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.cat_food += 50
            cprint(f'{self.name} сходил в магазин за едой коту', color='magenta')
        else:
            cprint(f'{self.name} деньги кончились', color='red')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я кот {self.name}, сытость {self.fullness}'

    def sleep(self):
        self.fullness -= 10
        cprint(f'Кот {self.name} спал весь день', color='green')

    def eat(self):
        self.fullness += 20
        cprint(f'Кот {self.name} поел', color='yellow')

    def tears_wallpaper(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint(f'Кот {self.name} драл обои', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice_cat = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice_cat == 1:
            self.tears_wallpaper()
        elif dice_cat == 2:
            self.eat()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50
        self.cat_food = 0
        self.mud = 0

    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}'


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_in_to_house(house=my_sweet_home)

cat = Cat(name='Харлей')
citizen.pick_up_a_cat(cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
    cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    print(cat)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
