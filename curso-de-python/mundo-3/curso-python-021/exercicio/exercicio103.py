def ficha(nome, gol=0):
    print(f'o jogador {nome} fez {gol} gols')

n = str(input('Nome do jogador: '))
g = str(input('Quantidade de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    n = 'Desconhecido'


else:
    print(f'"O jogador {n} fez {g} gol(s) no campeonato."')