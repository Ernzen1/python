"""
Count - Itertools
"""

from types import GeneratorType
from itertools import count

contador = count(5, -0.1)  # Iterador
for valor in contador:
    print(round(valor, 2))
    if valor > 1024:
        break