jogadores = {}
dadosIndividuais = []

while True:
    print('-' * 40)
    jogadores['nome'] = str(input('Digite o nome do Jogador: '))
    jogadores['partidas'] = int(input('Quantas partidas ele jogou? '))

    gol = []

    for g in range(1, jogadores['partidas'] + 1):
        gol.append(int(input(f'Quantos gols ele fez na {g}ª partidas? ')))

    jogadores['gols'] = gol
    jogadores['totalGols'] = sum(gol)

    dadosIndividuais.append(jogadores.copy())

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('-' * 40)
print(f'{"Pos":^5} {"Nome":^10} {"Gols":^15} {"Total":^5}')

for i, n in enumerate(dadosIndividuais):
    print(f'{i + 1:^5} {str(n["nome"]):^10} {str(n["gols"]):^15} {str(n["totalGols"]):^5}')

print('-' * 40)

while True:
    dados = int(input(f'De qual jogador você quer ver os dados? (Digite 999 para encerrar.) '))
    if dados == 999:
        break

    elif dados < 1 or dados >= len(jogadores["nome"]):
        print('ERRO! A posição desse jogador não existe.')

    else:
        jogador = dadosIndividuais[dados - 1]
        print(f'-- DADOS INDIVÍDUAIS DO JOGADOR {jogador["nome"]}')
        print('-' * 35)
        for i, v in enumerate(jogadores['gols']):
            print(f'No \033[33m{i + 1}º\033[m jogo ele fez \033[32m{v}\033[m gols.')