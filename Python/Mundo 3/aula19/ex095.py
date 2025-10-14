# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from time import sleep
time = []
while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for p in range(partidas): # p = partidas
        gols.append(int(input(f'Gols na partida {p+1}:')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time += [jogador]  # tem a mesma função que time.append(jogador)
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<6}')
print('-' * 50)
sleep(1)
for i in range(len(time)):
    dados = time[i]
    print(f'{i:<4}{dados["nome"]:<15}{str(dados["gols"]):<20}{dados["total"]:<6}')
    sleep(1)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        print('Encerrando...')
        break
    if busca >= len(time) or busca < 0:
        print('Erro! Código inválido.')
    else:
        print(f'-- DESEMPENHO DO JOGADOR {time[busca]["nome"].upper()} --')
        for i in range(len(time[busca]['gols'])):
            print(f'Jogo {i+1}: {time[busca]["gols"][i]} gols')
    sleep(1)










