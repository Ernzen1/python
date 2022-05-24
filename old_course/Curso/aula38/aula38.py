"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend
min, max -> mínimo e máximo
range -> Alcance, retorna um objeto range
A função list() -> transforma um objeto iterável em uma lista.

"""

# texto = "valor"
# #         0    1    2    3    4
# lista = ["A", "B", "T", "D", "E"]  # Uma lista é uma variável com vários valores.
# lista[4] = "Qualquer loucura"
# string = "ABacanaCDE"
# print(string[1])  # Só suporta um único valor
# print(lista[::-1])  # Suporte vários tipos de valores, em índices diferentes

# l1 = [1, 2, 3]
# l2 = [4, 5, 6, 7, 8, 9, 10, 11]
# l3 = list(range(1,10, 9))

# print(l2)
# l1.extend(l2)  # l1 extende a l2!
# l2.append("b")  # Insere um valor no último índice da lista
# l2.insert(0, "bananada")  # Insire um valor no indice selecionado
# l2.pop()  # remove o último elemento da lista
# del(l2[0])

# print(l1)
# print(max(l2))
# print(min(l2))
# print(l3)

# l2 = list(range(0, 700, 9))
# soma = 0
# for valor in l2:
#     soma += valor
#     print(valor)
#     print(soma)

# l2 = ["String", True, 10, -29.5]

# for elem in l2:
#     print(f"O tipo de elem é {type(elem)}")

secreto = "perfume"
digitadas = []  # Ele vai lembrar os caracteres certos, pois será armazenado na lista "digitadas"
chances = 5

while True:
    if chances <= 0:
        print("Você perdeu")
        break
    letra = input("Digite uma letra: ")
    if letra in digitadas:
        print("Essa letra já foi digitada! Tente outra letra!")
        continue
    if len(letra) > 1:
        print("Isso não vale! Digite apenas uma letra!")
        continue
    digitadas.append(letra)
    if letra in secreto:
        print("Acertou!")
    else:
        print(f"A letra {letra}, não existe na palavra secreta")
        digitadas.pop()
    secreto_temp = ""
    for letra_secreto in secreto:
        if letra_secreto in digitadas:  # Aqui ele valida quais letras estão em digitadas
            secreto_temp += letra_secreto  # se estiver em digitadass será concatenada a string
        else:
            secreto_temp += "*"  # Se não será adicionado uma "*" no lugar.

    if secreto_temp == secreto:
        print(f"Você ganhou! A palavra era {secreto_temp}")
        print(secreto_temp)
        break
    else:
        print(f"A palavra secresta está assim: {secreto_temp}")
    if letra not in secreto:
        chances -= 1

    print(f"Você errou! Você ainda tem {chances} chances")
    print()








