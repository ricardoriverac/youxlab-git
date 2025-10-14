continuacao= 'S'
jogadores=[]
while continuacao != 'N':
    nome=str(input('Digite o nome do jogador: '))
    partidas= int(input(f'Quantas partidas {nome} jogou? '))
    gols=[]
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}?')))
    jogador= {'NOME': nome, 'PARTIDAS': partidas, 'GOLS': gols}
    jogadores.append(jogador)
    continuacao=str(input('Deseja continuar? [S/N]').upper())
    print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

busca=-1
while busca != 999:
    busca= int(input('Mostrar dados de qual jogador? (999 encerra):'))
    if busca>len(jogadores):
        print(f'ERRO! não existe jogador com este código!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[busca]["NOME"]}')
        for i , g in enumerate (jogadores[busca]['GOLS']):
            print(f'No jogo {i+1} fez {g} gols')
        print('<<VOLTE SEMPRE!')