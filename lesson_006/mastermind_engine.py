from random import randint

number = 1000


def make_number():
    global number
    number = randint(number, 9999)
    return str(number)


def check_number(user_number):
    global number
    bulls = {'bulls': 0}
    cows = {'cows': 0}
    str_number = str(number)
    for digit in range(4):
        if str_number[digit] == user_number[digit]:
            bulls['bulls'] += 1
        elif str_number[digit] == user_number[0]:
            cows['cows'] += 1
        elif str_number[digit] == user_number[1]:
            cows['cows'] += 1
        elif str_number[digit] == user_number[2]:
            cows['cows'] += 1
        elif str_number[digit] == user_number[3]:
            cows['cows'] += 1
    return bulls, cows


