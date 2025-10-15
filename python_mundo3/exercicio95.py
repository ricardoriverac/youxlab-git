jogadores = {}
gols = []
jogador = []
c = 0
while True:
    jogadores['nome'] = str(input("Nome do jogador: ")).upper()
    partidas = int(input(f"Quantas partidas {jogadores['nome']} jogou: "))
    for c in range(1,partidas+1):
        gols.append(int(input(f"Quantos gols ele fez na {c} partida: ")))
    jogadores['gols'] = gols[:]
    jogadores['total'] = sum(gols)
    jogador.append(jogadores.copy())
    resp = str(input("Quer continuar [S/N]: ")).upper()
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]: ")).upper()
    if resp  in "N":
        break
print(f"Cod.nome            gols       Total")
print(f"-"*35)
for i,v in enumerate(jogador):
    print(f"{i: <4} {v['nome']: <2}       {v['gols']}      {v['total']:^4}")
print("-"*35)
while c != 999:
        break