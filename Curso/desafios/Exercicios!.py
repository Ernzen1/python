"""
Faça um programa que peça ao usuário para digitar um número inteiro,
infome se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informa que não é um número inteiro.
"""
# Pedir ao usuário (input) -> para digitar um número inteiro
# Checar se o número é par ou impar -> if ... % 2 = 0: -> elif ... % 2 = 1:
# Else: Esse não é nem um número!

num = input("Digite um número inteiro: ")  # Usuário digita uma entrada

if num.isdigit():  # Programa verifica se a entrada é um dígito.
    num = int(num)  # Se for dígito, o programa transformará a entrada em inteiro

    if num % 2 == 0:  # Aqui ela verifica se a divisão do inteiro resulta 0
        print(f"O número {num} é par!")  # Se sim "Esse número é par"

    elif num % 2 != 0:
        print(f"O número {num} é impar!")  # Se não, "Esse número é impar"


else:
    print("Isso não é nem um número!")  # Caso não seja digito retorna "Isso não é nem um número"


