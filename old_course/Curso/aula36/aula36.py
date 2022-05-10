"""
Como iterar strings com while
Se o elemento tem índices ele é iterável
Iterar é passar por cada elemento da string
"""
#        Índices
#        0123456789.......................33
frase = "o rato roeu a roupa do rei de roma"  # Iterável
tamanho_frase = len(frase)
print(frase[5])
contador = 0
nova_string = ""
usuario = input("Qual letra deseja colocar maiúscula? ")

# Iteração -> Iterar = o ato de percorrer cada elemento do elemente iterável.

while contador < tamanho_frase:  # control + / comenta tudo
    # print(frase[contador], contador) # O contador se torna o índice!
    letra = frase[contador]
    if letra == usuario:  # Como a string é imutável, só estamos alterando a "nova_string"
        nova_string += usuario.upper()  # O .upper(), coloca a string em caixa alta! utualmente a string é "u"
    else:
        nova_string += letra
    # nova_string += frase[contador]  # Concatenando a string vazia com a string frase
    contador += 1
    print(nova_string)

print(nova_string)
