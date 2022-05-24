"""
Desempacotamento de listas em Python

"""
lista = ["Luiz", "João", "Maria", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10000]
n1, n2, *outralista, n4 = lista  # O * indica que a variável vai armazenar todos os valores da lista numa lista.
print(outralista, n4)
