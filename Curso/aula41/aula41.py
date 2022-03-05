"""
Split -> Divir uma string, divide a lista tomando como divisor o caractere inserido.
Join -> Juntar uma lista
Enumerate -> Enumerar os elementos da lista -> Somente elementos iteráveis

"""

# string = "O Brasil é o país do futebol, o Brasil é penta, masjjsaa."
# lista = string.split(" ")  # transformando a string em uma lista.
# lista2 = string.split(",")
#  print(lista)
#  print(lista2)
#  palavra = ""
#  contagem = 0
#
# for valor in lista2:
#     print(valor.strip().capitalize())  # Capitalize deixa a primeira letra da string em maiúsculo
#       print(f" A palavra {valor} apareceu {lista.count(valor)} vezes na frase")
#      qtd_vezes = lista2.count()  # Strip remove o espaço do ínicio e do fim da string
#      if qtd_vezes > contagem:
#          contagem = qtd_vezes
#     #    palavra = valor
#
# print(f"A palavra que apareu mais vezes é {palavra} ({contagem}x)")

# string = "O Brasil é penta"
# lista = string.split(" ")
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])  # lista[indice] é igual a valor!

lista = [[0, "Guilherme"], [1, "Adriana"], [2, "Mariana"]]

for indice, nome in lista:
    print(indice, nome)

lista = [[0, "Guilherme"], [1, "Adriana"], [2, "Mariana"]]

for indice, nome in enumerate(lista):
    print(indice, nome)

n1, n2, n3 = lista  # Desempacotando a lista -> cada variável pegara um valor de um index.
print(n2)
