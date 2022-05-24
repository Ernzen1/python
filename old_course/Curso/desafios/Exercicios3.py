"""
Faça um programa que peça a primeiro nome do usuário.
Se o nome tiver 4 letros ou menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras,
escreva "Seu nome é normal"; maior que 6 escreva: "Seu nome é muito grande"
"""

# relacionar a viriável ao input, usar len para verificar o tamanho e comparar nos ifs

nome = input("Digite seu primeiro nome: ")

if nome.isascii():

    if len(nome) <= 4:
        print("Seu nome é muito curto!")

    elif 5 < len(nome) < 6:
        print("Seu nome é normal!")

    else:
        print("Seu nome é muito grande!")

else:
    print("Isso aí nem é um nome!")
