jogador = {}
dadosJogador = []
jogadores = []
print('-'*50)
print('             CADASTRANDO JOGADORES DE FUTEBOL:   ')
print('-'*50)
resp = 'S'
escolha_jogador = 0
while resp == 'S':
    jogador.clear()
    jogador['nome'] = str(input('-> Nome do Jogador: '))
    jogador['qtd_partidas'] = int(input('-- Quantas partidas jogadas: '))
    jogador['gols_em_partidas'] = []
    jogador['soma_gols'] = 0
    for g in range(jogador['qtd_partidas']):
        gols = int(input(f'     Quantos gols jogador fez na partida {g+1}: '))
        jogador['gols_em_partidas'].append(gols)
        jogador['soma_gols'] += gols
    jogadores.append(jogador.copy())
    resp = str(input('-- Deseja continuar? [S/N]: ')).upper().strip()

print(' cod ', end='')
for k in jogador.keys():
    print(f'{k:<25}', end='')
print()
print('-'*50)

for i, jog in enumerate(jogadores):
    print(f'{i:>4} ', end='')
    for dado in jog.values():
        print(f'{str(dado):<25}', end='')
    print()

print()
print('-'*50)
escolha_jogador = -1
while escolha_jogador < 0 or escolha_jogador >= len(jogadores):
    escolha_jogador = int(input('-- Mostrar dados de qual jogador? (999 para parar): '))
while escolha_jogador != 999:
    print('-'*50)
    print(f'LEVANTAMENTO DO JOGADOR {jogadores[escolha_jogador]["nome"]}')
    for p, g in enumerate(jogadores[escolha_jogador]['gols_em_partidas']):
        print(f'    Na partida {p+1} fez {g} gols.')
    escolha_jogador = -1
    while escolha_jogador < 0 or escolha_jogador >= len(jogadores):
        escolha_jogador = int(input('-- Mostrar dados de qual jogador? (999 para parar): '))