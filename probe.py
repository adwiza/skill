import logging.config
import numpy as np
from primes_package.main import print_primes
from log_settings import log_config

logging.config.dictConfig(log_config)
print_primes(30)

A = [[4, 2],
     [9, 0]]

B = [[3, 1],
     [-3, 4]]

C = np.dot(B, A)

print(C)

D = [[2, 1],
     [-3, 0],
     [4, -1]]

E = [[5, -1, 6],
     [-3, 0, 7]]

F = np.dot(D, E)

print(F)

G = [[1, 2, 3]]
H = [[4],
     [5],
     [6]]
I = np.dot(H, G)

print(I)
