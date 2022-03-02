entrada = input("Você quer converter para binário, octal ou hexadecimal? ")

if entrada == "binario" or entrada == "binary" or entrada == "bi" or entrada == "binário":
    num = int(input("Escreva seu número em decimal, octal ou hexadecimal: "))
    num = bin(num)
    print(f"O número em binário é: {num}")

elif entrada == "octal" or entrada == "oct" or entrada == "oc":
    num = int(input("Escreva seu número em decimal, binario ou hexadecimal: "))
    num = oct(num)
    print(f"O número em octal é: {num}")

elif entrada == "hexadecimal" or entrada == "hexa" or entrada == "hex":
    num = int(input("Escreva seu número em decimal, binario ou hexadecimal: "))
    num = hex(num)
    print(f"O número em hexadecimal é: {num}")

else:
    print("Entrada errada!")
