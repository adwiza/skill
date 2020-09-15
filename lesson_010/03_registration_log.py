# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

import re
from time import sleep


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


data = []
err_data = []
with open('registrations.txt', 'r') as f:
    for line in f:
        line = line[:-1]
        line = line.split(' ')
        if len(line) == 3 or str(line).isalpha():
            dog = '@'
            dot = '.'
            if dog in line[1] and dot in line[1] and 10 < int(line[2]) < 99:
                data.append(line)
        if len(line) != 3:
            err_data.append(line)
        elif not str(line[0]).isalpha():
            err_data.append(line)
        elif dog not in line[1] and dot not in line[1]:
            err_data.append(line)
        elif not 10 < int(line[2]) < 99:
            err_data.append(line)


for i in data:
    account = data.pop()
    with open('valid_registration.txt', 'a') as f:
        registered_user = ' '.join(account) + '\n'
        f.write(registered_user)

for e in err_data:
    invalid_user = err_data.pop()
    with open('invalid_registration.txt', 'a') as f:
        unregistered_user = ' '.join(invalid_user) + '\n'
        f.write(unregistered_user)
