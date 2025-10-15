'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome, gols):
    if not nome:
        nome = 'desconhecido'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
print(ficha(nome, gols))