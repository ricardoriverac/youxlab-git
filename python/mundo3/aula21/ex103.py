#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols durante a partida.')
nome_jogador = input('Qual o nome do jogador: ')
gols_jog = input(f'Quantos gols o {nome_jogador} fez durante a patida: ')
if nome_jogador.strip() == '':
    nome_jogador = 'Desconhecido'
if gols_jog.isnumeric():
    gols = int(gols_jog)
else:
    gols = 0
ficha(nome_jogador, gols)



