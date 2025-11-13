def ficha(jogador = '<desconhecido>', gols = 0):
    print('-' * 27)
    print(f'O jogador {jogador} fez {gols} gol(s) na partida.')

#Código Principal
print('-' * 27)
nomeJogador = str(input('Digite o nome do jogador: '))
quantidadeGol = str(input('Quantos gols o jogador fez: '))

if quantidadeGol.isnumeric():
    quantidadeGol = int(quantidadeGol)
else:
    quantidadeGol = 0

if nomeJogador.strip() == '':
    ficha(gols=quantidadeGol)
else:
    ficha(nomeJogador, quantidadeGol)