time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    partidas.clear()
    for c in range(total):
        partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
    
    jogador['gols'] = partidas[:] 
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())  
    
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if resposta == 'N':
        break

print('-=' * 30)
print(f'{"cod":<4}', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)

for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=' * 30)

