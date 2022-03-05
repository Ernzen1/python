"""
For / Else
Break -> Saí do loop
Contniue -> Reinicia o loop
"""

variavel = ["Guilherme", "Texto", "PPOOREORE", "PAPAPAPAPAP"]

for valor in variavel:
    if valor.lower().startswith("g"):  # .lower() -> converte as letras em minúsculas

        continue
    print(valor)
else:
    print("Não existe uma palavra que começa com G")
