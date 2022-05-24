"""
Sempre leia a documentação do python, desde que a linguagem sempre é atualizada.
Python é linguagem de tipagem dinâmica
Python não converte um tipo de dados automaticamente

isnumeric isdigit isdecimal -> Verifica se o dado pode ser convertido para decimal
-1 -> Somente chega números naturais e inteiros
"""

"""num1 = (input("Digite um número: "))
num2 = (input("Digite outro número: "))

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

else:
    print("Não pude converter os números para realizar contas")
"""

try:
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    num2 = int(num2)
    num1 = int(num1)
    print(num1 + num2)
except:
    print("error")
