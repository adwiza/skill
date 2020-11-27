import logging


def perky(param):
    return param / 0


log = logging.getLogger('perky')
log.setLevel(logging.INFO)
file_handler = logging.FileHandler('perky.log', 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
log.addHandler(file_handler)

number = 42

try:
    log.info('Посмотрим, как у него получится...')
    perky(number)
    log.info('Он смог!')
except Exception:
    log.exception(f'Дерзкий не справился с {number}')

# В больших программах практически всегда необбходимо разделять сообщения в логах
# по некоторому признаку - типы сооббщений, места возникновения, используемый модуль и тд
# Для этого можно создавать объекты логирования и конфигурировать их

