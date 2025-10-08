resultados = dict()

while True:
    resultados['nome_do_jogador'] = str(input("Qual o nome do jogador: "))
    resultados['partidas'] = int(input("Quantas partidas o jogador jogou?: "))
    resultados['gols'] = list()
    resultados['total'] = 0
    for jogo in range(resultados['partidas']):
        print(f"Gols {jogo}")
        gols = int(input("Quantos gols ele acertou?: "))
        resultados['gols'].append(gols)
    for index, gol in enumerate(resultados['gols']):
        resultados['total'] += gol
    resposta = str("Deseja continuar? [S/N]: ").upper
    if resposta == "S":
       resposta = str("Deseja continuar? [S/N]: ").upper  
    else:
        break 
    
print(f"No total ele acertou: {resultados['total']}")
print(resultados['gols'])
print(f"Na partida {index} o jogador marcou {gol} gols")