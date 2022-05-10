variavel = "valor"


def func():
    print(variavel)


def func2(arg=None):
    # global variavel  # Não é uma boa prática de programação.
    # variavel = "Outro valor"  # Só edita a variável localmente, essa variável é diferente da outra.
    # print(variavel)
    arg = arg.replace("l", "pppp")
    return arg


func()
variavel2 = func2(arg=variavel)

print(variavel2)
