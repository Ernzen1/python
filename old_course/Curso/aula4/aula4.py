"""
Tipos de dados:
str - string - Textos - "Assim" - 'Assim'
int - inteiro - 123456 - 0 - -10 - -20 - 15000
float - real/ponto flutante - 9.6 - -9.4 - 9.44444
bool - booleano/lógico - True / False - Usados em comparações - 10 == 10 -> retornaria true
"""
# Chamando a classe type, que retorna o tipo desse valor.
print(41, type(77))  # Número real, negativo, ou positivo
print('Luiz', type('Luiz'))  # Tudo que está em aspas é uma string (",')
print(25987.44, type(798.7777))  # Números com ponto, tendo pelo menos 1 casa decimal
print(10000 == 1111, type(1 == 1))  # checa a expressão para verificar se ela é verdadeira ou falsa
print('L' == 'L', type('1' == '1'))  # Não precisa Comparar só números
print(bool(''))  # avaliando uma string vazia -> Sempre falso
print('luiz', type('luiz'), bool('luiz'))  # Transformando um tipo de dados em outro
# Foi pego o valor 'luiz' e convertido para o bool de 'luiz' -> pode se fazer com int, float e str também;
# Chamado Type Casting

print('10' + '10') # concatena as strings com o operador '+, gerando 1010

# Nome: string
print('Guilherme Ernzen', type('Guilherme Ernzen'))

# Idade: Int
print(20, type(20))

# Altura: Float
print(1.85, type(1.85))

# É maior de idade? : Bool
print(20 > 18, type(20 > 18))









