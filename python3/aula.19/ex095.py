time = []
gols = []
jogador = dict()
escolha = 0
continuar = 'S'

while continuar == 'S':
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        gols.append(gol)
    continuar = str(input('Deseja continuar [S/N]'))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())

while escolha != 'nao':
    escolha = str(input('Mostrar dados de escolha jogador? (nao para parar) '))
    print(f' LEVANTAMENTO DO JOGADOR {jogador[escolha]["nome"]}:')
    for pos, g in enumerate(time[escolha]['gols']):
        print(f'No jogo {pos} fez {g} gols.')
print('-=-' * 15)
print(f' o jogador {jogador["nome"]} jogou {jogador["total"]} partidas e fez {jogador["gols"]} gols')
print('-' * 40)