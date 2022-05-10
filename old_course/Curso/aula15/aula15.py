"""
Operadores Lógicos

and -> Operador booleano and, todos tem que ser True para gerar o resultado True.
or -> Operador booleano or, apenas um dos comparativos precisa ser True para resultar em True.
not -> Operador booleano not, gera o efeito contrário dos outros operadores. Inversor!
in -> Operador booleano in, procura se certo valor está presente no expressão comparada
notin -> Operador booleano notin, procura se certo valor não está presente na expressão comparada

"""
"""
a = 9
b = a ** 5
if not b > a:
    print("B é maior que A")
else:
    print("A é maior que B")

a = ''  # Strings vazias são consideradas valores nulos
b = 0  # Zero é um valor falso para a operação booleana

if not b:  # Se não tiver valor em b, ou seja, se b for falso
    print("Preencha um valor para B")"
"""

nome = "Guilherme"

if 'u' not in nome:
    print("Existe a letra u no seu nome")
else:
    print("Não existe a letra u no seu nome")

if 'u' in nome:
    print("Existe a letra u no seu nome")
else:
    print("Não existe a letra u no seu nome")
