import logging

log = logging.getLogger('primes')
# log.setLevel(logging.DEBUG)
# fh = logging.FileHandler("primes.log", 'w', 'utf-8')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# log.addHandler(fh)


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        print(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                print(f'делится на {prime}')
                break
        else:
            print(f'Найдено новое простое {number}')
            prime_numbers.append(number)
            yield number


for prime in prime_numbers_generator(100):
    print(f'Простое из генератора {prime}')
