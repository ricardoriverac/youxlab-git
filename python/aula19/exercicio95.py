time = []
jogador = {}
lista = []
partidas = 0
while True:
    jogador.clear()
    lista.clear()
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input(f'Digite a quantidade de partidas que {jogador["nome"]} jogou: '))
    for g in range(0, partidas):
        lista.append(int(input(f'Quantidade de gols da partida {g}: ')))
    jogador['gols'] = lista[:]
    jogador['total'] = (sum(lista))
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end = ' ')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >=len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    NO jogo {i+1} fez {g} gols.')