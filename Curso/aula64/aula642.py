s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2
s4 = s1 | s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s2 ^ s1

print("Essa é a interseção: ", s3)
print("Essa é a união:", s4)
print("Essa é a diferença de s1 e s2: ", s5)  # Só retorna o que está no set da esquerda e não está na direita.
print("Essa é a diferença de s2 e s1: ", s6)
print("Essa é a diferença simétrica: ", s7)

l1 = ["Luiz","Luiz","Luiz","Luiz","Luiz","Luiz","Luiz","Luiz","Luiz","Luiz","Luiz","Luiz", "Maria", "João"]
l2 = ["João", "João", "João", "João", "João", "João", "João", "João", "João", "João", "Maria", "Luiz" ]

l1 = set(l1)
l2 = set(l2)
print(l1 == l2)

l1 = list(l1)
l2 = list(l2)
print(l1, l2)