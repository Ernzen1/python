"""
Em tuplas não se pode mudar os índices / valores das tuplas

"""

t1 = (1, 2, 3, 4, 5, 6, 7)
t1 = list(t1)
t1[1] = 0
t1 = tuple(t1)

print(t1)