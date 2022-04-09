"""
List comprehension


"""

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [var for var in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
print(l2, ex2, ex3)