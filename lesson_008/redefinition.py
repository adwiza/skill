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

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


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


# r2d2 = WarRobot(model='R2D2', gun='machinegun')
# print(r2d2)
# r2d2.operate()
#
# roomba = VacuumCleaningRobot(model='M505')
# print(roomba)
# roomba.operate()

sub_robot = SubmarineRobot(model='DD5', gun='torpedo')
print(sub_robot)
sub_robot.operate()
