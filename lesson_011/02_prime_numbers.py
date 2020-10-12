# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import math


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


get_prime_numbers(n=10)


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def get_prime_numbers(self):
        self.i += 1
        for prime in self.prime_numbers:
            if type(self.i % prime == 0) is None:
                return False
        return True

    def __next__(self):
        while self.i < self.n:
            if self.get_prime_numbers():
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    """Возвращает все простые от 2 до n"""
    sieve = set(range(2, n))
    for i in range(2, int(math.sqrt(n))):
        if i in sieve:
            sieve -= set(range(2 * i, n, i))
    return sorted(sieve)


for number in prime_numbers_generator(n=10000):
    print(number)

digits = []
set_of_items = set()
simple_num = prime_numbers_generator(100000)
for s in simple_num:
    if len(str(s)) == 3:
        digits.append(str(s))
        filtered = filter(lambda lucky: lucky[:1] == lucky[-1:], digits)
        set_of_items.update(filtered)
    elif len(str(s)) == 4:
        digits.append(str(s))
        first_digit = str(s)[:1]
        second_digit = str(s)[1:2]
        third_digit = str(s)[-1:]
        four_digit = str(s)[-2:-1]
        left = int(first_digit) + int(second_digit)
        right = int(third_digit) + int(four_digit)
        if left - right == 0:
            set_of_items.add(str(s))
    elif len(str(s)) == 5:
        digits.append(str(s))
        first_digit = str(s)[:1]
        second_digit = str(s)[1:2]
        third_digit = str(s)[-1:]
        four_digit = str(s)[-2:-1]
        left = int(first_digit) + int(second_digit)
        right = int(third_digit) + int(four_digit)
        if left - right == 0:
            set_of_items.add(str(s))

print(sorted(set_of_items))

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
