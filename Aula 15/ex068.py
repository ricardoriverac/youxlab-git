from random import randint
ganho = 0
while True:
    jogador = int(input('digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    abra = ' '
    while abra not in 'PI':
        abra = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {}'.format(jogador, computador, total), end='')
    print('saiu par' if total % 2 == 0 else 'saiu impar')
    if abra == 'P':
         if total % 2 == 0:
             print('Você ganhou!')
             ganho += 1
         else:
            print('Você perdeu, infelizmente')
            break
    elif abra == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            ganho += 1
        else:
            print('Você perdeu, infelizmente')
            break
    print('Tente jogar de novo')
print('VOCÊ CONSEGUIU ME VENCEEER EM {} VEZES'.format(ganho))



