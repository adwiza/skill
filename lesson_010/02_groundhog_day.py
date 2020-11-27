# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint
import logging_

ENLIGHTENMENT_CARMA_LEVEL = 777
carma_level = 0
carma_counter = 0
logging_.basicConfig(filename="log.txt", level=logging_.ERROR)


def one_day():
    dice = randint(1, 6)
    if dice == 1:
        return dice
    elif dice == 2:
        return dice
    elif dice == 3:
        return dice
    elif dice == 4:
        return dice
    elif dice == 5:
        return dice
    elif dice == 6:
        return dice


while True:
    if carma_level == ENLIGHTENMENT_CARMA_LEVEL:
        break
    elif carma_level > ENLIGHTENMENT_CARMA_LEVEL:
        carma_level = 0
        carma_counter += 1
    else:
        probability = randint(1, 13)
        if probability == 1:
            alert = randint(1, 6)
            if alert == 1:
                logging_.error('IamGodError')
                raise BaseException("IamGodError")
            elif alert == 2:
                logging_.error('DrunkError')
                raise BaseException("DrunkError")
            elif alert == 3:
                logging_.error('CarCrashError')
                raise BaseException("CarCrashError")
            elif alert == 4:
                logging_.error('GluttonyError')
                raise BaseException("GluttonyError")
            elif alert == 5:
                logging_.error('DepressionError')
                raise BaseException("DepressionError")
            elif alert == 6:
                logging_.error('SuicideError')
                raise BaseException("SuicideError")

    carma_level += one_day()
    print(f'Уровень кармы {carma_level}')
    print(f'Счётчик кармы {carma_counter}')

# https://goo.gl/JnsDqu
