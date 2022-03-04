entrada = input("Você quer converter para binário, octal ou hexadecimal? ")

if entrada == "binario" or entrada == "binary" or entrada == "bi" or entrada == "binário":
    num = input("Escreva seu número em decimal: ")
    if num.isnumeric():  # Verifica se a entrada é um número
        num = int(num)  # Transforma a string em int
        num = bin(num)  # Transforma o número em binário com o cabeçalho "0b"
        num_bi = []  # Criando uma lista iterável

        # Transformando o número inteiro numa lista para remover o cabeçalho
        for num_final in num:  # Iterando o int num.
            num_bi += num_final  # Concatenando a int num em cada índice da "num_final"
        del num_bi[0:2]  # Deletando o cabeçalho "0b" da lista

        # Tranformando a lista em string, para ser printada direito.
        string_temp = ""  # definindo a string temp para receber os indexes da lista "num_bi"
        for string in num_bi:  # iterando uma lista em outra
            string_temp += string  # adicionando em "string" um valor dos indexes de num_bi a cada loop.
        print(f"O número em binário é {string_temp}")

    else:
        print("Isso não é um número!")


elif entrada == "octal" or entrada == "oct" or entrada == "oc":
    num = input("Escreva seu número em decimal: ")
    if num.isnumeric():
        num = int(num)
        num = oct(num)
        num_oc = []

        for num_final in num:
            num_oc += num_final

        del num_oc[0:2]
        string_temp = ""

        for string in num_oc:
            string_temp += string
        print(f"O número em binário é {string_temp}")

    else:
        print("Isso não é um número!")

elif entrada == "hexadecimal" or entrada == "hexa" or entrada == "hex":
    num = input("Escreva seu número em decimal: ")
    if num.isnumeric():
        num = int(num)
        num = hex(num)
        num_hex = []

        for num_final in num:
            num_hex += num_final
        del num_hex[0:2]

        string_temp = ""
        for string in num_hex:
            string_temp += string

        print(f"O número em hexadecimal é {string_temp}")
    else:
        print("Isso não é um número!")

else:
    print("Entrada errada!")
