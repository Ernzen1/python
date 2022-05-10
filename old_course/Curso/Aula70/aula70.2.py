import sys
import time


# def gera():
#     variavel = "Valor 1"
#     yield variavel
#     variavel = "Valor 2"
#     yield variavel
#     variavel = "Valor 3"
#     yield variavel
#     variavel = "Valor 4"
#     yield variavel
#
#
# g = gera()
# #
# # print(hasattr(g, "___iter___"))
# # print(hasattr(g, "___next___"))
#
# for var in g:
#     print(var)
#

l1 = [x for x in range(10024)]  # Listas retem todos os valores na memória
l2 = (x for x in range(10024))  # Geradores não retem todos os valores na memória
print(sys.getsizeof(l2))
print(sys.getsizeof(l1))
for v in l2:
    print(v)