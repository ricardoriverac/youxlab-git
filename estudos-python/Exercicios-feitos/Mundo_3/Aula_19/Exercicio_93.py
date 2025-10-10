jogador = {}
golsFeitos = []
jogador['nome'] = input('Qual o nome do jogar?')
quantidadePartida = int(input('Quantas partidas'))
contagem = 0
soma = 0
for c in range (quantidadePartida):
    golsFeitos.append(int(input(f'Quanto gols ele fez na partida {c}: ')))
    jogador['gols'] = (golsFeitos.copy())
    soma += golsFeitos[c]
jogador['total'] = soma
print (jogador)
for k, v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print (f'O jogador {jogador["nome"]} jogou {quantidadePartida} partidas')
for p in range (0,quantidadePartida):
    print (f'Na partida {p}, fez {jogador["gols"][p]}')
print (f'Foi um total de {jogador["total"]} gols')