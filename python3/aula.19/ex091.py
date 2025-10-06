from random import randint
from time import sleep
listaordenada = []
for i in range(0, 4):
    jogadas = {'numjogador': i, 'jogada': randint(0, 10)}
    if i == 0:
        listaordenada.append(jogadas)
        print(f'jogador{i} tirou {jogadas["jogada"]}')
        
    elif jogadas['jogada'] < listaordenada[-1]['jogada']:
        listaordenada.append(jogadas)
        print(f'jogador{i} tirou {jogadas["jogada"]}')
        sleep(1)
    else:
        for pos, d in enumerate(listaordenada):
            if jogadas['jogada'] > d['jogada']:
                listaordenada.insert(pos, jogadas)
                print(f'jogador{i} tirou {jogadas["jogada"]}')
                sleep(1)
                break
print('=-'*15)
print('    RANKING DE JOGADORES    ')
sleep(1)
for v, c in enumerate(listaordenada):
    print(f'{v+1} LUGAR: jogador{c["numjogador"]} com valor {c["jogada"]} ')
    sleep(1)