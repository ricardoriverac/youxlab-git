# resposta = str(input("Qual biblioteca ou função você deseja saber?: "))
# help(resposta)
# print("fim")


resposta = "S"

while resposta != "N":
    resposta = str(input("Qual biblioteca ou função você deseja saber?: "))
    help(resposta)
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
print("fim")
