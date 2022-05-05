"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem Importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ["Gui", "Dri", "Ana", "Isa", "Fran"]

for grupo in combinations(pessoas, 3):
    print(grupo)