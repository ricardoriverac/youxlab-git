from random import randint
from time import sleep
dicionario = []
print('=-'*13)
print('     JOGO DA SORTE     ')
print('=-'*13)
for j in range(0, 4):
    jogadas = {'numjogador': j, 'jogada': randint(0, 10)}
    if j == 0:
        dicionario.append(jogadas)
        print(f'-> jogador {j} tirou {jogadas["jogada"]}')
        
    elif jogadas['jogada'] < dicionario[-1]['jogada']:
        dicionario.append(jogadas)
        print(f'-> jogador {j} tirou {jogadas["jogada"]}')
        sleep(1)
    else:
        for pos, d in enumerate(dicionario):
            if jogadas['jogada'] > d['jogada']:
                dicionario.insert(pos, jogadas)
                print(f'-> jogador{j} tirou {jogadas["jogada"]}')
                sleep(1)
                break
print('=-'*20)
print('->->->-> RANKING DE JOGADORES->->->->')
print('=-'*20)
sleep(1)
for v, c in enumerate(dicionario):
    print(f'-{v+1} LUGAR: jogador {c["numjogador"]} com valor {c["jogada"]} ')
    sleep(1)