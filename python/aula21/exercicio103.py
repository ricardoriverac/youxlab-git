def jogador(nome = '<desconhecido>', gols = 0 ):
    print(f'O jogador {nome} fez {gols} gol(s).')

jog = str(input('Nome: '))
gol = str(input('Gols: '))
jogador(jog, gol)
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    jogador(gols=gol)
else: 
    jogador(jog, gol)
'''
o isnumeric irá ler a string digitad e fará a "validação" para descobrir se o que foi digitado é ou não é um número
'''