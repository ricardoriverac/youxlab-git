def ficha(nome=0, gols=0):
    nome = input('Nome: ')
    gols = input('Gols: ')
    if nome == 0 or nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no  campeonato.')