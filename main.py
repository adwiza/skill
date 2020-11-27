import logging

from primes import prime_numbers_generator

main_log = logging.getLogger('main')
# main_log.setLevel(logging.DEBUG)
# main_file_handler = logging.FileHandler('main.log')
# main_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# main_file_handler.setFormatter(main_formatter)
# main_log.addHandler(main_file_handler)


def print_primes(n):
    for prime in prime_numbers_generator(n):
        main_log.info(f'Простое число из генератора {prime}')


if __name__ == '__main__':
    print_primes(n=10)
