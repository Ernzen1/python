"""
Zip - Unindo Iteráveis
ZIp_longest - Itertools
"""
from itertools import zip_longest, count
indice = count()  # Gerador sem fim
cidades =["Florianópolis", "Belo Horizonte","Osasco", "Cajuzeiro", "Curitiba"]

estados = ["SC", "MG", "SP", "BA"]

cidades_estados = zip(estados, cidades, indice)  # Retorna um iterádor com a função next()


for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)

