"""
1- Crie uma função que exibe uma saudação com os paramêtros saudação e nome.

2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles

3- Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne
(return) o valor do primeiro número somado ao percentual do mesmo.

4- Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for
divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e 3 retorne fizz buzz, se não, retorne
o número enviado.
"""


# 1
# def saudacao(msg="Bom dia querido ", nome="Guizão"):
#     print(msg, nome)
#
#
# saudacao()


# 2
#
# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
#
#
# soma(8, 9, 4)

# 3

# def soma_percentual(v1, v2):
#     print(v1 + (v1 * v2 / 100))
#
#
# soma_percentual(50, 10)

# 4

def fizzbuzz(v1):
    if v1 % 5 == 0 and v1 % 3 == 0:
        return "Fizz Buzz"
    if v1 % 3 == 0:
        return "Fizz"
    if v1 % 5 == 0:
        return "Buzz"

    return v1


from random import randint

for i in range(1000):
    alea = randint(0, 1000)
    print(fizzbuzz(alea))


