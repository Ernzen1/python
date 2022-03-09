"""
Funções - def
As funções são criadas para evitar repitições.
Repetir é errado.
"""


def saudacao(msg="Olá ", nome="João sem nome"):  # Foi criado uma variável no parametro
    nome = nome.replace("e", "3")  # A função executa o bloco de códigos quando é chamada
    msg = msg.replace("i", "99")
    # print(msg, nome)  # Não é comumente usado.
    return f"{msg}{nome}"


variavel = saudacao()

print(variavel)