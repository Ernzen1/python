# Entrada de dados

# input("Qual o seu nome? ")  # Função que perguntará ao usuário algo
nome = input("Qual o seu nome? ")  # Atribuindo uma variação ao input
print(f'O usuário digitou {nome} e o tipo da viriável é '
      f'{type(nome)}')  # a função input sempre vai retornar uma string

idade = input("Qual a sua idade? ")
ano_nascimento = 2022 -int(idade)  # Já que o input retorna uma string não é possível fazer a conta
# Foi feito um cast para mudar o tipo da variável para int
print()  # prints vazios pulam uma linha no shell
print(f'{nome} nasceu em {ano_nascimento} e o tipo da viriável é '
      f'{type(ano_nascimento)}')


