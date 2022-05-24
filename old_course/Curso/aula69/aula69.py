"""
Compreensão de dicionários
"""

lista = [
    ("Chave", "Valor"),
    ("chave2", "valor2"),
]

# d1 = {x: x * 8 for x, y in enumerate(range(10))}
d1 = {f"chave_{x}": x**2 for x in range (5)}
print(d1)
