def jogador(nome = ' ', gols = ' ' ):
    if nome in '':
        nome = '<desconhecido'
    if gols < '1':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s).')

jog = str(input('Nome: '))
gol = str(input('Gols: '))
jogador(jog, gol)