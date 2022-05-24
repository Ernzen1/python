"""
Condições!
if -> fará uma comparação, se retornar verdadeiro, vai relizar uma ação, precisa ser acompanhado de : -> SE
elif -> uma segunda condição, deve ser posta abaixo do if! Pode ser repetido.
Sempre é executado o primeiro e ignorado os demais-> Se não
else -> quando nenhuma expressão for verdadeira, retornará o else, não pode ser utilizado sozinho! -> Se não²
Os comandos procuram por condições verdadeiras para executar o código
Para ser considerado o código dentro da comparação if.
O mesmo deverá estar dentro de uma hierarquia de 4 espaços abaixo do if
"""

if False:  # Os códigos dentro do if precisam estar quatro espaços para direita, em questão de hierarquia
    print("Verdadeiro")
    num_1 = 2
    num_2 = 2
    print(num_2 + num_1)
elif True:  # Executado esse por ser  primeiro
    nome = input("Qual seu nome? ")
    print(f'Seu nome é {nome}')

elif True:  # Ignorado esse pois, existe outra função elif verdadeira acima dessa
    print("Agora é falso")

else:
    print("Não é verdadeiro")

# print('A minha expressão é falsa') Está fora da hierarquia, então é considerado fora do if/else/elif
