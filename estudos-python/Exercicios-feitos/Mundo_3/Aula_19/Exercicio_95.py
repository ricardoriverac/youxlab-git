jogador = {}
todoJogador = []
golsFeitos = []
contagem = 0
soma = 0
while True:
    jogador['nome'] = input('Qual o nome do jogador?\n->').strip().capitalize()
    quantidadePartida = int(input('Quantas partidas?\n->'))
    for c in range (quantidadePartida):
        golsFeitos.append(int(input(f'Quanto gols ele fez na partida {c}?\n->')))
        jogador['gols'] = (golsFeitos.copy())
        soma += golsFeitos[c]
    jogador['total'] = soma
    soma = 0
    todoJogador.append(jogador.copy())
    print (jogador)
    golsFeitos.clear()
    opcao = input('Você quer continuar?\n Se não for digite "N" ou "n": ').strip().upper()
    if opcao == 'N':
        break
busca = 0
while True:
    busca = int(input('Qual jogador você gostaria de ver os dados?\nSe quiser encerrar digite 999!\n->'))
    if busca == 999:
        break
    while busca<0 or busca>len(todoJogador):
        print('Esse número está fora do alcance da lista!')
        print('Escreva um número dentro do alcance da lista!')
        busca = int(input('Qual jogador você gostaria de ver os dados?\nSe quiser encerrar digite 999!\n->'))
    print(todoJogador[busca])