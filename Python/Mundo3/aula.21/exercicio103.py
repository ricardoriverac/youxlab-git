def ficha(nome='< desconhecido >', gols=0):

    if nome == '':
        
        nome = '< desconhecido >'
    if gols.isnumeric():
        gols = int(gols)
    else:

        gols =0
    print(f'O jogador {nome},fez {gols} gols essa partida')
    return 0

nome = str(input('Digite o nome:'))
gols = str(input('Digite o numero de gols: '))
f = ficha(nome,gols)
print(f)