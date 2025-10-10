def ficha(jogador='desconhecido', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')


# principal
n = str(input("Nome do jogador: "))
g = str(input("Gols feito pelo jogador: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
