"""
Funções def
"""


def funcao(var):  # Se não tiver return a função retorna NONE -> um não valor, nada.
    print("Isso não será executado")
    return var  # Sempre que a função encontrar um return ela


variavel = funcao("Valor que eu quero")

if variavel:
    print(variavel)
else:
    print("Nenhum valor")


