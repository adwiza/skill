class Employee:
    """ Работник """

    def salary(self):
        """ Зарплата """
        return 15000


class Parent:
    """ Родитель """

    def childrens(self):
        """ Дети """
        return ['Вася', 'Катя']


class Man(Parent, Employee):
    """ Человек является и родителем и работником """
    pass


me = Man()
print(me.childrens())
print(me.salary())
