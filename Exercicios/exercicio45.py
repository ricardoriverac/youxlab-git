import random
opcao1=("Pedra")
opcao2=("Papel")
opcao3=("Tesoura")
lista=[opcao1, opcao2, opcao3]
computador=random.choice(lista)
print("Escolha sua opção:\n"
"1: Pedra\n"
"2: Papel\n"
"3: Tesoura")
jogador=(input("Sua escolha: "))

if jogador==1:
    jogador="Pedra"
elif jogador==2:
    jogador="Papel"
elif jogador==3:
    jogador="Tesoura"

print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}")