# def funq(arg, arg2):
#     return arg * arg2
#
#
# var = funq(2, 3)
#
# a = lambda x, y: x * y
#
# print(a(2, 2))

lista = [
    ["P1", 13],
    ["P2", 14],
    ["P3", 17],
    ["P4", 4],
    ["P5", 9],
    ["P0", 5],
    ["P7", 2],
    ["P9", 1]
]


# lista.sort(key =lambda item: item[1], reverse=True)
print(sorted(lista, key=lambda i: i[0]))

