# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 50
        self.mud = 0

    def __str__(self):
        return f'В доме еды осталось еды {self.food}, кошачьего корма {self.cat_food}, денег осталось {self.money}, ' \
               f'грязь {self.mud}'

    def add_mud(self):
        self.mud += 5
        if self.mud > 90:
            serge.happiness -= 10
            masha.happiness -= 10


class Husband:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.money = 0
        self.total_money = 0
        self.total_food_husband = 0
        self.house = None

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}, степень счастья {self.happiness}'
        # return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода...', color='red')
        elif self.happiness < 10:
            cprint(f'{self.name} умер от депресии...', color='red')
            return

        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.play_WoT()

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} заехал в дом!!!', color='cyan')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
            self.total_food_husband += 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.total_money += 150
        self.fullness -= 10

    def play_WoT(self):
        cprint(f'{self.name} играл в World of Tanks целый день', color='green')
        self.happiness += 20
        self.fullness -= 10

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} погладил кота', color='blue')


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.fur_coat = 0
        self.total_food_wife = 0
        self.house = None

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}, степень счастья {self.happiness}'
        #return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умерла от голода...', color='red')
        elif self.happiness < 10:
            cprint(f'{self.name} умерла от депресии...', color='red')
            return

        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.cat_food_shopping()
        elif self.house.mud > 100:
            self.clean_house()
        elif dice == 1:
            self.bay_fur_coat()
        # elif dice == 2:
        #     self.clean_house()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.eat()

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} заехала в дом!!!', color='cyan')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
            self.total_food_wife += 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 10
            cprint(f'{self.name} сходила в магазин за едой', color='magenta')
        else:
            cprint(f'{self.name} деньги кончились', color='red')

    def cat_food_shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.cat_food += 50
            cprint(f'{self.name} сходила в магазин за едой коту', color='magenta')
        else:
            cprint(f'{self.name} деньги кончились', color='red')

    def bay_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.fullness -= 10
            self.happiness += 60
            self.fur_coat += 1
            cprint(f'{self.name} купила шубу', color='yellow')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} погладила кота', color='yellow')

    def clean_house(self):
        self.house.mud -= 100
        self.fullness -= 10
        cprint(f'{self.name} убралась в доме', color='yellow')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


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
        self.fullness += 10
        self.house.cat_food -= 5
        cprint(f'Кот {self.name} поел', color='yellow')

    def tears_wallpaper(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint(f'Кот {self.name} драл обои', color='red')

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} заехал в дом!!!', color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint(f'Кот {self.name} умер...', color='red')
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


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.happiness = 100
        self.house = None

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}, степень счастья {self.happiness}'
        # return super().__str__()

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 3
        cprint(f'{self.name} родился', color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint(f'Малыш {self.name} умер от голода...', color='red')
            return

        dice = randint(1, 6)
        if self.fullness < 10:
            self.eat()
        elif dice == 1:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            cprint('Малыш {} поел'.format(self.name), color='yellow')
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 3
        cprint(f'Малыш {self.name} поспал', color='green')




######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
harley = Cat(name='Харлей')

serge.go_in_to_house(house=home)
masha.go_in_to_house(house=home)
murzik.go_in_to_house(house=home)
harley.go_in_to_house(house=home)
kolya.go_in_to_house(house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    harley.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(harley, color='cyan')
    cprint(home, color='cyan')

cprint('Итоги года: Шуб  было куплено {}, денег заработано {}'.format(masha.fur_coat, serge.total_money),
       color='magenta')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

