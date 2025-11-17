import random
from time import sleep

jogos = []

numerosAleatorio = 0

quantidadeJogos = int(input('Digite a quantidade de jogos que você deseja criar: '))

for c in range(0, quantidadeJogos):
    numerosEscolhidos = []

    for ns in range(0, 7):
        numerosAleatorio = random.randint(1, 60)

        if numerosAleatorio not in numerosEscolhidos:
            numerosEscolhidos.append(numerosAleatorio)

    jogos.append(numerosEscolhidos[:])
    numerosEscolhidos.clear()

print('-' * 35)
print(f'{"JOGO SORTEADO":^35}')
print('-' * 35)

for i, jogo in enumerate(jogos):
    print(f'{i + 1}º Jogo: \033[33m{jogo}\033[m')
    sleep(1)

print('-' * 35)
print('Esses foram todos o jogos sorteados.')
print('-' * 35)
print(f'\033[32m{"BOA SORTE!":^35}\033')
print('-' * 35)