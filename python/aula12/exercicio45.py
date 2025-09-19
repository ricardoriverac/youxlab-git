#pedra, papel e tesoura
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[computador]} \nJOgador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    if jogador == 2:
        print('JOGADOR PERDEU')

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('JOGADOR PERDE')
    elif jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR VENCEU')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDE')
    if jogador == 2:
        print('EMPATE')
else:
    print('indisponível')