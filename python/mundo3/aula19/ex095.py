#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.


jogador = {}
cont = 'S'
while cont == 'S':
    jogador = {}
    jogador["nome"] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for p in range(partidas):
        q = int(input(f"Quantos gols na partida {p + 1}? "))
        gols.append(q)
        jogador["gols"] = gols
        jogador["total"] = sum(gols)
    print(jogador)
    print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
    for i, g in enumerate(jogador["gols"]):
        print(f'Na partida {i + 1}, fez {g} gols.')
    print(f'Total de gols: {jogador["total"]}')
    cont = input('Você deseja cadastrar mais jogador?[S/N] ').upper()