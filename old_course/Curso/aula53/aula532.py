# def divisao(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
#
# divid = divisao(9, 8)
#
# if divid:
#     print(divid)
# else:
#     print("Conta inválida")
#
#
# def f(var):
#     print(var)
#
#
# def dumb():
#     return f  # Se não utilizar os parantereses a função não é executada
#
#
# var = dumb()
# print(id(var), id(f))
#
# if var == f:
#     print(f"{var} é igual a {f}")
#
# else:
#     print(f"{var} não é igual a {f}")

def dumb():
    return "Luz", "Agua", "KKKK"


var = dumb()

print(var[1], type(var))
