"""
Funções (def) - *args **kwargs
A partir do momento que se seta um padrão para um argumento
Todos após ele prescisam ter um valor padrão e nomealos.

"""


def dumb(*args, **kwargs):
    print(args, kwargs)
    idade = kwargs.get("nome")  # Verificando se há o argumento idade em kwargs
    if idade is not None:
        print(idade)
    else:
        print("A variável idade, não existe")


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
         29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
         29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
dumb(*lista, *lista2, nome="Luiz", nome2= "Guizão")  # Desempacotando a lista

