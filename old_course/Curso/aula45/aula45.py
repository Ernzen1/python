"""
Operador ternário em Python
"""

# logged_user = False
#
# # if logged_user:  # É identico a if logged_user == true
# #     mensagem = "Usuário logado"
# # else:
# #     mensagem = "Usuário precisa logar"
# #
# # print(mensagem)
#
# msg = "Usuário logado" if logged_user else "Usuário precisa logar"
# print(msg)

idade = input("Qual é a sua idade? ")
if not idade.isnumeric():
    print("Você precisa digitar apenas números")
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = "Pode acessar" if e_maior else "Não pode acessar"
    print(msg)
