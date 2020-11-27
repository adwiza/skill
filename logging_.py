import logging


def prime_number_generator(n):
    prime_numbers = []
    for number in range(2, n +1):
        logging.debug(f'{number}')
        for prime in prime_numbers:
            if number % prime == 0:
                logging.debug(f'делится на {prime}')
                break
        else:
            logging.debug(f'Найдено новое простое {number}')
            prime_numbers.append(number)
            yield number

 
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO, filename='primes.log')
  
for prime in prime_number_generator(100):
    logging.info(f'Простое из генератора {prime}')
