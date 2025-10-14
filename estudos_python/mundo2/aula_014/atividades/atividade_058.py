'''
Melhora o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.
'''

#Resposta

import random


print('''
    JOGO DE ADIVINHAÇÃO
=-=-=-=-=-=-=-=-=-=-=-=-=-=
    tente adivinhar o 
    número que estou 
    pensando!!! Dica,
    estou pensando em
    um número de 1 a 10!!
''')
computador = random.randint(1, 10)
palpites = 0
acertou = False
while acertou == False:
    digite_numero = int(input('\nDigite a sua primeira tentativa: '))
    if digite_numero == computador :
        acertou = True
        print(f'Você ACERTOU!!! Você tentou {palpites} vezes!!')

    else:
        if digite_numero > computador:
            print('ERROU!! Tente um número menor.')
            acertou = False
            palpites += 1

        elif digite_numero < computador:
            print('ERROU!! Tente um número maior. ')
            acertou = False
            palpites += 1
