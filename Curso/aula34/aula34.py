"""
While em Python - Aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira.

Precisa-se entender as condições e os operadores.
"""

"""
num = 0
while num < 10:  # Comando enquanto validando a condição
    if num == 3:  # Se for igual a 3 será somado 1 para sair do número e
        num += 1
        # continue  # Recomeça o loop
        break
    print(num)
    num += 1

print("It's Over")



x = 0  # Coluna

while x < 10:
    y = 0  # Precisa-se zerar o loop menor para poder-se avançar no loop maior.
    while y < 5:
        print(f"X vale {x} e Y vale {y}")
        y += 1

    x += 1  # x = x + 1

print("Acabou!")
"""

while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s]Sim e [n] Não ")

    if sair == "s":
        break
    elif sair == "n":
        pass
    else:
        print(f"{sair} não é um comando válido!")
        continue
    if not num_1.isnumeric() or not num_2.isnumeric():  # Checando se os inputs não são números.
        print("Você precisa digitar um número!")
        continue  # Se não forem números o loop é restartado.

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(num_1 + num_2)

    elif operador == "-":
        print(num_1 - num_2)

    elif operador == "/":
        print(num_1 / num_2)

    elif operador == "*":
        print(num_1 * num_2)

    else:
        print("Operador invalido")