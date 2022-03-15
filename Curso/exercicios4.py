"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2 executada.

2- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2 executada. Faça a função1 execu
tar duas funções que recebam um número difrente de argumentos.

"""


# def ola_mundo():
#     return "ola mundo"
#
#
# def master(funcao):
#     return funcao
#
# executando = master(ola_mundo())
# print(executando)


def func1(funq, *args, **kwargs):
    return funq(*args, **kwargs)


def funq2(nome):
    return f"Olá. {nome}"


def salute(nome, salutes):
    return f"{salutes} {nome}"


executando = func1(funq2, "Guizão")
executando2 = func1(salute, "Guizão", salutes="Buenos dias!")
print(executando)
print(executando2)
