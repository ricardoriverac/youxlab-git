import random
print('Vamos jogar jokenpô!')
jogador = str(input('Pedra, Papel ou Tesoura?')).lower()
computador = random.choice(['Pedra','Papel','Tesoura']).lower()
print(f'Voce escolheu {jogador}')
print(f' O computador escolheu {computador}')
if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") :
    print('Voce ganhou!')
elif (jogador == "papel" and computador == "pedra"):
    print('Voce ganhou!')
elif(jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Computador ganhou!")