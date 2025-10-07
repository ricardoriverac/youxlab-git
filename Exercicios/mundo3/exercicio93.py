resultados = dict()
resultados['nome_do_jogador'] = str(input("Qual o nome do jogador: "))
resultados['partidas'] = int(input("Quantas partidas o jogador jogou?: "))
resultados['gols'] = list()
resultados['total'] = 0

for jogo in range(resultados['partidas']):
    print(f"Gols {jogo}")
    gols = int(input("Quantos gols ele acertou?: "))
    resultados['gols'].append(gols)

print(resultados['gols'])
for index, gol in enumerate(resultados['gols']):
    print(f"Na partida {index} o jogador marcou {gol} gols")
    resultados['total'] += gol
print(f"No total ele acertou: {resultados['total']}")
