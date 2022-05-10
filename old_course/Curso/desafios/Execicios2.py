"""
Faça um programa que pergunta a hora ao usuário e baseando-se no horário descrito,
exiba a suadação apropiada. Ex: Bom dia! 0-11, Boa tarde! 12-17 e Boa noite! 18-23.
"""

# Primeiro criar uma variável para o nome do dia e também atrelar ela ao input.
# Segunda checar se o input é um dígito, se for, checar se o dígito está entre a hora inicial
# Relação elif para verificar as horas do dia.

hora = input("Digite a hora do dia: ")

if hora.isdigit():
    hora = int(hora)

    if 0 <= hora <= 11:
        print("Bom dia!")

    elif 12 <= hora <= 17:
        print("Boa tarde!")

    else:
        print("Boa noite!")

else:
    print("Isso não é um hora do dia!")
