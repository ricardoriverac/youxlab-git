jogador = {}
golsFeitos = []
contagem = 0
soma = 0
while True:
    jogador['nome'] = input('Qual o nome do jogador?')
    quantidadePartida = int(input('Quantas partidas?'))
    for c in range (quantidadePartida):
        golsFeitos.append(int(input(f'Quanto gols ele fez na partida {c}?: ')))
        jogador['gols'] = (golsFeitos.copy())
        soma += golsFeitos[c]
    jogador['total'] = soma
    soma = 0
    print (jogador)
    golsFeitos.clear()
    opcao = input('Você quer continuar?\n Se não for digite "N" ou "n": ')
    if opcao == 'N':
        break
for k, v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print (f'O jogador {jogador["nome"]} jogou {quantidadePartida} partidas')
for p in range (0,quantidadePartida):
    print (f'Na partida {p}, fez {jogador["gols"][p]}')
print (f'Foi um total de {jogador["total"]} gols')