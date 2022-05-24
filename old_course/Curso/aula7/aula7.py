nome = 'Guilherme'
idade = 20
altura = 1.85
e_maior = idade > 18
peso = 85
imc = peso / (pow(altura, 2))

print(nome, 'tem', idade, 'anos de idade e seu IMC é: ', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
# fstrings ->strings que é possível colocar {}, sem fazendo-se desnecessário o uso das vírgulas, precisam do f no ínicio
# :.2f -> se refere ao números de casa decimais após a virgula que irá apresentar após o print.
# A sintax é : -> ponto -> (Número de casas) -> tipo de dado.


print('{} tem {} anos de idade e seu imc é {:.2f}' .format(nome, idade, imc))  # .format são ponteiros igual ao C.
# No .format é preciso usar a delimitação de casas decimais dentro das chaves não no ponteiro.
# pode-se ordernar os ponteiros, seguindo a ordem crescente dos ponteiros declarados em .format
# a ordem é sempre começada pela primeira posição, considerada 0.

print('{n} tem {i} anos de idade e seu imc é {im:.2f}' .format(n=nome, i=idade, im=imc))
# pode-se denominar as variáveis por outros nome tomando como o exemplo acima.

