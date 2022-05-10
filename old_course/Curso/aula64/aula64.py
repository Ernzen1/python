"""
Sets -> Não respeitam ordens, não suportam elementos duplicados!
add -> Adiciona
update -> atualiza
clear -> limpa
discard -> descarte
union -> une, utiliza-se o PIPE |
intersection & -> todos os elementos presentes nos dois sets
difference -> elementos apenas no set da esquerda
symmetric_difference -> Elementos que estão nos dois sets, mas não em ambos
"""

s1 = set()
s1.add("1")  # Não itera
s1.add("2")

s1.discard("2")
print(s1)
s1.update("Python")  # Itera sobre o elemento no set, não respeita a ordem
s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8, 9, 1})
for v in s1:
    print(v)


l1 = [1,2,3,4,1,21,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,3,2,1,9]
l2 = [1,2,3,4,5,6,7,8,9,10,11,1,1]
print(l1)
l1 = set(l1)
l2 = set(l2)
l1 = l1 | l2
print(l1)
l1 = list(l1)
print(l1)