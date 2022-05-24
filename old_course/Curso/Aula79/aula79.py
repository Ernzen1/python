from itertools import groupby

alunos = [
    {"nome": "Guilherme", "nota": 10},
    {"nome": "Netin", "nota": 0},
    {"nome": "Gaga", "nota": 1},
    {"nome": "Barbie", "nota": 9},
    {"nome": "Gil", "nota": 8},
    {"nome": "Jader", "nota": 7},
    {"nome": "Bigas", "nota": 1},
    {"nome": "Guarana", "nota": 2},
    {"nome": "Anathan", "nota": 3},
    {"nome": "Francina", "nota": 5},
]
ordena = lambda item: item["nota"]  # Ordena os dados
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f"agrupamento: {agrupamento}")
    quantidade = len(list(valores_agrupados))
    print(f"{quantidade} alunos tiraram a nota {agrupamento}")