from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):

        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}, еды осталось {self.food}, денег осталось {self.money}'

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.money += 50
        self.fullness -= 10

    def eat(self):
        if self.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def play_DOTA(self):
        cprint(f'{self.name} играл в доту целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            self.money -= 50
            self.food += 50
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
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()


beavis = Man(name='Бивис')
batthead = Man(name='Батхед')
for day in range(1, 365):
    print(f'============= день {day} ==============')
    beavis.act()
    batthead.act()
    print(beavis)
    print(batthead)


# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print(vasya)
