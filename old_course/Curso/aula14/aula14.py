"""

Operadores relacionas
== -> Compara dois valores, se são iguais
!= -> Compara dois valores, se um é diferente do outro
> -> Compara dois valores, se um é maior que o outro
< -> Compara dois valores, se um é menor que o outro
>= -> Compara dois valores, se um é maior, ou igual a outro
<= -> Compara dois valores, se um é menor, ou igual a outro

Sempre que forem executados, irá retornar uma expressão booleana.
Podem comparr todos os tipos de dados primitivos! -> str, int, float e bool
"""
variavel = 'valor'  # Afirmação que 'valor' é igual a variavel
print(2 == 2)  # Estou pergutando se 2 é igual a 2

# Comparando uma string com um número inteiro
num_1 = 2
num_2 = '2'
print(num_1 == num_2)

# Comparando se a string e o inteiro são diferentes
expressao = num_1 != num_2
print(expressao)

# Comparando bool com bool

expressao1 = True == False
print(expressao1)