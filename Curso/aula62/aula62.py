d1 = {
    "Key 1" : "valor1",
    "Key 2": "Valo2r",
    "Key 3" : "Tupla",
    "Key 4" : None
}
# d1["doenstexist"] = "Now it exists"
# if "doenstexist" in d1:
#     print(d1["doenstexist"])
# d1.setdefault(0)
# d1.update({"nova_chave": "Novo valor"})
# d1["epilepsia"] = "Morri"
# if d1.get("nova_chave") is not None:
#     print((d1.get("nova_chave")))
# print(d1)
# print(d1["str"])
#
# print("valor1" in d1.values())

for k, p in d1.items():
    print(k, p)
    