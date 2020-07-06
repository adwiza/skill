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
        cprint(f'{self.name} заехал в дом!!!', color='cyan')

class House:

    def __init__(self):
        self.food = 10
        self.money = 50

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

for day in range(1, 366):
    print(f'============= день {day} ==============')
    citizen.act()
    citizen.act()
    print('---------------в конце дня-----------------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)


# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print(vasya)
