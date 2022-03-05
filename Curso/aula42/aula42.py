"""
Enumerate - Enumerar elementos da lista.
"""

lista = [ ["Edu", "João", "Luiz"], ["Maria", "Aline", "Joana"], ["Helena", "Ed", "Lu"] ]
# Cada lista tem indíce, então a "Maria" é igual ao index [1][0]

# enumerada = enumerate(lista)
# print(list(enumerada))  # type cast de objeto para lista!

for v1 in enumerate(lista, -78798789):  # Enúmera um elemento iterável em ordem crescente!
    valor_enumerador, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
