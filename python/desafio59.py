from random import randint
computador = randint(0, 10)
tentativas = 0  # contador de palpites
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while True:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1  # soma 1 a cada palpite
    if jogador == computador:
        print(f'Parabéns! Você acertou o número {computador}!')
        break  # sai do laço quando acerta
    elif jogador < computador:
        print('Mais... tente novamente!')
    else:
        print('Menos... tente novamente!')
print(f'Você precisou de {tentativas} palpites para acertar.')
