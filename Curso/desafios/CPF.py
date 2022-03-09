"""
CPF = 168.995.350-09
--------------------------------------------------------------------------------------
1 * 10 = 10                 #  1 * 11 = 11
6 * 9 = 54                  #  6 * 10 = 10
8 * 8 = 64                  #  8 * 9 = 72
9 * 7 = 63                  #  9 * 8 = 72
9 * 6 = 54                  #  9 * 7 = 63
5 * 5 = 25                  #  5 * 6 = 30
3 * 4 = 12                  #  3 * 5 = 15
5 * 3 = 15                  #  5 * 4 = 20
0 * 2 = 0                   #  0 * 3 = 0
                            #  0 * 2 = 0
                                              343
                                          11 - (343 % 11) = 9
297                                       Digito 2 = 9
11 - (297 % 11) = 11
11 > 9 = 0  -> Maior que 9 será sempre zero # if not ... > 9

Digito 1 = 0
"""
from random import randint
num = str(randint(100000000, 999999999))
cpf2 = num
reverso = 10  # Contador reverso
total = 0

for index in range(19):
    if index > 8:  # O primeiro índice vai de 0 a 9
        index -= 9  # Os mesmos são os 9 primeiros dígitos do CPF

    total += (int(cpf2[index]) * reverso)  # Valor total da multiplicação

    reverso -= 1  # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        cpf2 += str(d)
print(f"O CPF gerado é: {cpf2}")

