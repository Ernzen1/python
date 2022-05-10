nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

jovem = 20
velho = 30

if jovem <= idade <= velho:
    print(f"{nome} pode pegar o empréstimo!")

else:
    print(f"{nome} não pode pegar o empréstimo!")
