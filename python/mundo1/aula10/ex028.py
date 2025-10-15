#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero_advinhar = random.randint(0,5)
tentativa = 1
max_tentativas = 5
while tentativa < max_tentativas:
    tentativa += 1
palpite = int(input('Advinhe o número que estou pensando: '))
if palpite < numero_advinhar:
    print('Número muito baixo, tente novamente!')
elif palpite > numero_advinhar:
    print('Muito alto, tente novamente')
else:
    print(f'Muito bem, você acertou {numero_advinhar}, em {tentativa} tentativas!')


