x = 10
y = "Gui"
z = "Ernzen"
x, y = y, x  # Invertendo os valores das variáveis
x, y, z = z, x, y  # Nada mais que alinhando os valores
print(f"{x}, {y}, {z}")