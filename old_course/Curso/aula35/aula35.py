"""
While / Else
contadores
acumuladores
"""

contador = 1  # Conta valores de forma linear
acumulador = 1  # Acumula valores a cada volta do loop

while contador <= 10:
    print(contador, acumulador)
    if contador > 5:
        break
    acumulador += contador
    contador += 1
else:  # Pode ser usado para loops também! Mas, somente será executado se a expressão passar a ser falsa
    # Se houver um break, ou algo que termine o loop, o else será pulado.
    print("Cheguei no else!")

print("Pulei o else!")
