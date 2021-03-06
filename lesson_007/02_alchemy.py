# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        new_object = Air()
        if other.name == 'Огонь':
            new_object.name = Lightning()
            return new_object.name
        elif other.name == 'Земля':
            new_object.name = Dust()
            return new_object.name
        else:
            new_object.name = None
            return new_object.name


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        new_object = Fire()
        if other.name == 'Земля':
            new_object.name = Lava()
            return new_object.name
        else:
            new_object.name = None
            return new_object.name


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return 'Земля'


class Water:

    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        new_object = Fire()
        if other.name == 'Воздух':
            new_object.name = Storm()
            return new_object.name
        elif other.name == 'Огонь':
            new_object.name = Steam()
            return new_object.name
        elif other.name == 'Земля':
            new_object.name = Mud()
            return new_object.name

        else:
            new_object.name = None
            return new_object.name


class Steam:
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return 'Пар'


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return 'Шторм'


class Mud:
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return 'Грязь'


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return 'Молния'


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return 'Пыль'


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return 'Лава'


print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.