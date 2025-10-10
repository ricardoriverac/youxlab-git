from random import randint
computador = randint(0, 10)
print('Sou o computador... Acabei de pensar em um numero entre 0 e 10.')
print('Você consegue advinhar qual foi? ')
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente outra vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))