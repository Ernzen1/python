"""
Variaveis são um nome de algo que é definido para salvar algo na memória do computador.
Devem sempre iniciar com letra, podem conter números, separar sempre por _, letras minúsculas
"""

nome = 'Guilherme'  # Este valor ('Guilherme') está atribuido a variável nome.
idade = 20  # int
altura = 1.85  # float
e_maior = idade > 18  # bool
peso = 85  # int
IMC = peso / (pow(altura, 2))  # Ou peso / altura ** 2

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print('É Maior?', e_maior)

print(idade * altura)  # Realiza a multiplicação em float pois, é int * float

print(nome, 'tem ', idade, 'anos de idade e seu IMC é: ', IMC)

