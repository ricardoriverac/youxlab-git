'''
Faça um programa que tenha uma função chamada ficha(), que receba dois 
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
algum dado não tenha sido informado corretamente.
'''

#Responda

def ficha():
    nome = input('Nome do jogador: ').strip()
    gols = input('Número de gols: ').strip()

    if nome == '':
        nome = '<desconhecido>'

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s).')

ficha()
