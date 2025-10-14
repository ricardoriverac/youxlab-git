def ficha(nome=0, gols=0):
    nome = input('digite o nome: ')
    gols = input('digite a quantidade de gols: ')
    if nome == 0 or nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O/a jogador(a) {nome} fez {gols} gols.')





ficha()
