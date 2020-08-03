class Cat:
    has_tail = True
    woolliness = 20

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} {} есть хвост, {}, пушистость - {}'.format(self.__class__.__name__, self.name, self.has_tail,
                                                              self.woolliness)


class Bobtail(Cat):
    has_tail = False


class Sphinx(Cat):
    woolliness = 1


murzik = Bobtail(name='Мурзик')
sonya = Sphinx(name='Соня')


# print(murzik)
# print(sonya)

class Robot:

    def __init__(self, model, *agrs, **kwargs):
        super().__init__(*agrs, **kwargs)
        self.model = model

    def __str__(self):
        result = super().__str__()
        return result + ' {} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class CanFly():

    def __init__(self, *agrs, **kwargs):
        super().__init__(*agrs, **kwargs)
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100  # метров
        self.velocity = 300  # км/ч

    def fly(self):
        self.altitude = 5000  # метров

    def land_on(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def operate(self):
        super().operate()
        print('Летим')

    def __str__(self):
        result = super().__str__()
        return result + ' {} Высота {} скрость {}'.format(self.__class__.__name__, self.altitude, self.velocity)


class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print('Роот охраняет объекты с помощью', self.gun)

    def __str__(self):
        return '{} model {} Стой, Стрелять буду!'.format(self.__class__.__name__, self.model)


class SubmarineRobot(WarRobot):

    def operate(self):
        super().operate()
        print('Охрана ведется под водой')


class VacuumCleaningRobot(Robot):
    def __init__(self, model):
        super().__init__(model=model)
        self.dust_bag = 0

    def operate(self):
        print('Робот пылесосит пол, заполненность мешка для пыли {}'.format(self.dust_bag))


class Drone(CanFly, Robot):

    # def __init__(self, model):
    #     super().__init__(model=model)
    #     CanFly.__init__(self)

    def operate(self):
        super().operate()
        print('Робот ведет разведку с воздуха')

    def __str__(self):
        return '{} model {} '.format(self.__class__.__name__, self.model) + \
           '{} Высота {} скрость {}'.format(self.__class__.__name__, self.altitude, self.velocity)

# r2d2 = WarRobot(model='R2D2', gun='machinegun')
# print(r2d2)
# r2d2.operate()
#
# roomba = VacuumCleaningRobot(model='M505')
# print(roomba)
# roomba.operate()

# sub_robot = SubmarineRobot(model='DD5', gun='torpedo')
# print(sub_robot)
# sub_robot.operate()


drone = Drone(model='Orbiter II')
drone.take_off()

print(drone)
drone.fly()
print(drone)
drone.operate()
print(drone)
drone.land_on()
print(drone)

#sdfsdfsdfsdfsdfs