"""
Como verificar a quantidade de caracteres!
Função len() -> Funciona com string e outros tipos de dados, não funciona com tipos numéricos.
len() -> Também conta espaços, o retorno é sempre inteiro
inteiros, float, booleans não tem len()

"""
"""
usuario = input("Digite seu usário : ")
qtd_crc = len(usuario)
if qtd_crc < 6:
    print("Digite mais caracteres!")
else:
    print("Você foi cadastrado no sistema!")
"""

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")
print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')