"""

Manipulando strings - Aula 6
String indices -> São index, endreços dos caracteres, na string.
Fatiamento de strings [inicio:fim:passo]
Funções buit-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

"""
# positivos
texto = "Python"  # Em orderm o python considera o texto como por exemplo "Python" = [012345] ou [54321]

print(texto[:-4])  # Colocando o indice da string se acessa o caractere presente naquele endereço
url = "google.com/"
print(url[:-1])

nova_string = texto[-4:-1]  # para fatiar a string, foi indicado o começo do fatiamento [2 e o fim :6].
# Nem o caractere do começo, nem o caractere do fim são incluídos. Se não colocar o começo, ele reconhece como 0
# Se colocar somente o começo, ele só irá pegar daquele caractere pra frente.
print(nova_string)

nova_string2 = texto[0:6:4]  # O último informa quantos caracteres ele terá que pular.
# Se ficar em branco é subentendido para ele pular de um em um.
print(nova_string2, len(nova_string2))
