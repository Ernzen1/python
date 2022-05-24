"""

* Criar variáveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variável com o o atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casa decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando f-strings

"""

nome = 'Guilherme'
idade = 20
altura = 1.85
peso = 85.0
ano = 2022
nascimento = 2001
imc = peso / pow(altura, 2)

print(f'{nome} tem {idade} anos de idade, pesa {peso:.1f} kg, tem {altura:.2f} de altura,', end=' ')
print(f'nasceu no ano de {nascimento}, tem o imc de: {imc:.3} e vive no meio de uma guerra no ano de {ano}.', end=' ')
