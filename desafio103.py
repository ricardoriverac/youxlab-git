def ficha(nome='<desconhecido>', gols=0):
    """
    -> Mostra a ficha de um jogador.
    :param nome: nome do jogador (opcional)
    :param gols: número de gols marcados (opcional)
    :return: sem retorno
    """
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")
n = str(input("Nome do jogador: ")).strip()
g = str(input("Número de gols: ")).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == "":
    ficha(gols=g)
else:
    ficha(n, g)