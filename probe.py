import  logging.config

from primes_package.main import print_primes
from log_settings import log_config

logging.config.dictConfig(log_config)
print_primes(30)