from random import randint
computador = randint(0, 10)
print('Estou gerando um numero entre 0 e 10')
print('Será que você consegue acertar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou == True
    else:        
        print(f'Acertou com {palpites} tentativas. Parabens!')