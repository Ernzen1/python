"""
List comprehension


"""

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [var for var in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v,v2) for v in l1 for v2 in range(3)]  # Criado a tupla de v e v2,

l3 = ["Luiz", "Mauro", "Maria"]
ex4 = [v.replace("a", "@").upper() for v in l3]
tupla = (
    ("chave", "valor"),
    ("chave2", "valor2")
)

ex5 = [(y,x) for x, y in tupla]

l4 = list(range(100))
ex6 = [v for v in l4 if v % 3 == 0 if v % 8 == 0]
ex7 = [v if v % 3 == 0 else v * 2 for v in l4]
print(ex7)