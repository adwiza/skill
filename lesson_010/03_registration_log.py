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

data = []
err_data = []
with open('registrations.txt', 'r') as f:
    for line in f:
        line = line[:-1]
        try:
            line = line.split(' ')
            if len(line) == 3 or str(line).isalpha():
                dog = '@'
                dot = '.'
                if dog in line[1] and dot in line[1] and 10 < int(line[2]) < 99:
                    data.append(line)
            else:
                err_data.append(line)

        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc} в строке {line}')


for i in data:
    account = data.pop()
    with open('valid_registration.txt', 'a') as f:
        registered_user = ' '.join(account) + '\n'
        f.write(registered_user)

#print('error_data', err_data, len(err_data))
