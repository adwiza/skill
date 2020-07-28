class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def __init__(self, name):
        self.name = name

    def inspect(self):
        print(self.__class__.__name__, self.name)  # Ссылка на класс объекта и далее на имя объекта
        print('Всего ног:', self.legs)
        print('Хвост присутствует:', 'Да' if self.has_tail else 'Нет')
        print(self.__dict__)  # Подкапотный словарь аттрибутов


class Cat(Pet):
    """ Кошка является домашним животным """

    def sound(self):
        print('Мяу!')


class Bobtail(Cat):
    """ Бобтейл является Кошкой """

    has_tail = False


class Dog(Pet):
    """ Собака является домашним животным """

    def sound(self):
        print('Гав!')


class Hamster(Pet):
    """ Хомяк является домашним животным """

    def sound(self):
        print('Ццццц!')


# print('Котик')
# my_pet = Cat()
# my_pet.inspect()
# my_pet.sound()

# print('Бобтейл')
# my_pet = Bobtail('Терминатор')
# my_pet.inspect()
# my_pet.sound()
#
# print('Собака')
# my_pet = Dog()
# my_pet.inspect()
# my_pet.sound()
#
# print('Хомяк')
# my_pet = Hamster()
# my_pet.inspect()
# my_pet.sound()


# pet = Pet(name='Кузя')
# # pet.legs = 5
# pet.inspect()
# print(pet.__class__ is Pet)

class CanFly():

    def __init__(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def __str__(self):
        return '{} Высота {} скрость {}'.format(self.__class__.__name__, self.altitude, self.velocity)


class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1


class Aircraft(CanFly):

    def take_off(self):
        self.altitude = 1000
        self.velocity = 300

    def fly(self):
        self.velocity = 800


class Missile(CanFly):
    def take_off(self):
        self.velocity = 1000
        self.altitude = 10000

    def land_on(self):
        self.velocity = 0
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('БА-БАХ!')


# butterfly = Butterfly()
# print(butterfly)
# butterfly.take_off()
# print(butterfly)
# butterfly.fly()
# print(butterfly)
# butterfly.land_on()
# print(butterfly)

missile = Missile()
print(missile)
missile.take_off()
print(missile)
missile.fly()
print(missile)
missile.land_on()
print(missile)
