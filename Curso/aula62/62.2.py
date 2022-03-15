import copy
# clientes = {
#     "Cliente1" : {
#       "ID" : 1999,
#       "Nome" : "Guilherme",
#       "Sobrenome" : "Ernzen",
#     },
#     "Cliente2" : {
#       "ID" : 454544,
#       "Nome" : "Joãozinho",
#       "Sobrenome" : "Marçal",
#
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f"Exibindo {clientes_k}")
#     for dados_k, dados_v in clientes_v.items():
#         print(f"\t{dados_k} = {dados_v}")

# d1 = {1: "a", 2: "b", 3: "c", "d" : ["Guizão", "Ernzen"]}
# # v = d1.copy()  # Shallow copy of the dictionary
# v = copy.deepcopy(d1)
# v[1] = "Marçal"
# v["d"][0] = "Joãozin"  #
# # v[1] = "Guizão"  # Modifica ambos os dicionários, ambos os objetos apontam para o mesmo endereço de memória.
# print(v["d"][0])
# print(v)
# print(d1)

lista = [
    ["c1", 1],
    ["c2", 2],
    ["c3", 3],
    ["c4", 4],
    ["c5", 5],
    ["c",7],
]
d1 = dict(lista)
d2 = {
    "a" : 2,
    "b" : 3,
    "c" : 4,

}
print(d1)
d1.update(d2)
print(d1)