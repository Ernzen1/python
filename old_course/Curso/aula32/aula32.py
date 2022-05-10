"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de pontop flutuante (float)
:. (Número)f - Quantidade de casas deicimais (float)
: (Caractere) (> ou < ou ^) (Quantidade) (Tipo -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
print(f"{num1:0>10.3f}")  # Formatando com ":", tem que informar o dígito que preencherá e o número de casas
# Também pode ser utilizado para formatar como um tipo de dado, colocando:.(n casas) e o tipo do dado.
"""num2 = 3

divisão = num1 / num2
print("{:.2f}".format(divisão))  # As chaves representam a variável divisão
print(f"{divisão:.2f}")  # Ambos fazem a mesma função

nome = "Guilherme"
print(f"{nome:s}")  # Formatando a string como string
"""

