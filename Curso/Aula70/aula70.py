lista = [0,1,2,3,4,5]

# for v in lista:  # Transforma a lista em iterador.
lista = iter(lista)
print(next(lista))
print(hasattr(lista, "___next___"))
