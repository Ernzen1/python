"""
For -> Usado para loops que sabe-se o fim, ou são finitos.
While -> Usado para loops que não se sabe o fim, ou são infinitos.
Iterando strings com for
Função range(start = 0, stop, step = 1)
Pode ser usado para achar os multiplos de oito!
Continue - pula para o próximo loop
Break - Quebra o loop
"""

texto = "Phyton"

# for n, letra in enumerate(texto):  # Função enumerate, enumera a cada volta do loop.
#     print(n, letra)
# soma = 0
# for n in range(100):  # Por padrão, start = 0 e step = 1, o loop for, só irá para frente.
#     # É sempre um intervalo aberto, nunca conta o último algarismo, tomando como exmplo o 10.
#     if n % 8 == 0:
#         print(n)
texto = "Python"
nova_string = ""
for letra in texto:
    if letra == "t":
        continue
        nova_string = nova_string + letra.upper()
    elif letra == "h":
        nova_string = nova_string + letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
