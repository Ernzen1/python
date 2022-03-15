print()
print("Para responder as perguntas é só digitar somente a letra minúscula!")
print()
perguntas = {
    "Pergunta 1": {
        "pergunta": "Quanto é 2 + 2? ",
        "respostas": {"a": 3, "b": 4, "c": 5, "d": 9},
        "resposta_certa": "b"},
    "Pergunta 2": {
        "pergunta": "Quanto é 912 * 2? ",
        "respostas": {"a": 1824, "b": 1985, "c": 1174, "d": 2014, },
        "resposta_certa": "a"},
    "Pergunta 3": {
        "pergunta": "Em que ano Imperatriz Leopoldina nasceu? ",
        "respostas": {"a": 1798, "b": 1745, "c": 1797, "d": 1801, },
        "resposta_certa": "c"},
    "Pergunta 4": {
        "pergunta": "Hitler foi conmtemporâneo de quem?",
        "respostas": {"a": "D. Pedro II", "b": "Gengis Khan", "c": "Ronaldinho Gaúcho", "d": "Mano Brown", },
        "resposta_certa": "a"},
    "Pergunta 5": {
        "pergunta": "Qual é a raiz de 16777216 ? ",
        "respostas": {"a": 2578, "b": 3250, "c": 2560, "d": 4096, },
        "resposta_certa": "d"},
    "Pergunta 6": {
        "pergunta": "Ronaldinho Gaúcho fez quantos gols na carreira? ",
        "respostas": {"a": 521, "b": 305, "c": 512, "d": 452, },
        "resposta_certa": "b"},
    "Pergunta 7": {
        "pergunta": "Quem é o amor da minha vida? ",
        "respostas": {"a": "Adriana", "b": "É a opção a", "c": "Sim é a Adriana", "d": "É a Adriana", },
        "resposta_certa": "a"},
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    print()
    print("Escolha as opções abaixo:")
    for rk, rv in pv["respostas"].items():
        print(f"[{rk}]: {rv}")

    resposta_usuario = input("Sua resposta: ")
    if resposta_usuario not in pv["respostas"].keys():
        print("Essa não é uma opção!!")
    else:
        if resposta_usuario == pv["resposta_certa"]:
            print("Você acertou!!")
            print()
            respostas_certas += 1
        else:
            print("Você errou!!")
            print()

    total_perguntas = len(perguntas)
    porcentagem_acerto = respostas_certas / total_perguntas * 100
    if total_perguntas == respostas_certas:
        print(f"Você já acertou todas as perguntas!!!")
    elif respostas_certas > 3:
        print(f"Você já acertou {respostas_certas}!")
        print(f"Sua porcentagem de acerto foi de {porcentagem_acerto}%")
