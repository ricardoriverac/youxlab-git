def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s)')
    
    
nome=str(input('Digite o nome do jogador: '))
gols=str(input(f'Digite a quantidades de gols que {nome} fez: '))


if gols.isnumeric():
    gols = int(gols)
    if nome == '':
        ficha(gols=gols)
    else:
        ficha(nome,gols)
else:
    if nome == '':
        ficha()
    else:
        ficha(nome)
