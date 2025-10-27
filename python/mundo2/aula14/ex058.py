# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

import random
comput_jogada = random.randint(1,11)
print('----JOGO DO ADVINHE COM SEU COMPUTADOR----')
acerto = False
tentativa = 0
while not acerto:
    jogadora = int(input('Adivinhe o número que estou pensando de 1 a 10: '))
    tentativa += 1
    if jogadora == comput_jogada:
        acerto = True
print(f'Você acertou com {tentativa} tentativas!')
