# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
except ValueError as exc:
    if type(input_data) == str:
        print(f'Не тот тип данных должен быть {exc} а на самом деле {type(input_data)} в переменной {input_data}')
except IndexError as exc:
    print(f'Выход за границы массива {exc} переменной {input_data}')
except:
    print('Что-то пошло не так')
else:
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
