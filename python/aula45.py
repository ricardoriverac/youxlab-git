import random
opcoes = ["pedra", "papel", "tesoura"]
escolha_utilizador = input("Escolha pedra, papel ou tesoura: ").lower()
while escolha_utilizador not in opcoes:
    print("Opção inválida. Por favor, escolha entre pedra, papel ou tesoura.")
    escolha_utilizador = input("Escolha pedra, papel ou tesoura: ").lower()
escolha_computador = random.choice(opcoes)
print(f"\nVocê escolheu: {escolha_utilizador}")
print(f"Computador escolheu: {escolha_computador}\n")
if escolha_utilizador == escolha_computador:
    print("É um empate!")
elif (escolha_utilizador == "pedra" and escolha_computador == "tesoura") or \
     (escolha_utilizador == "papel" and escolha_computador == "pedra") or \
     (escolha_utilizador == "tesoura" and escolha_computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")