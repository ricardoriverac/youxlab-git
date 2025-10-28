'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo 
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

#Responda

#Declaração de variaveis
contador2 = contador = 0

while True:
    #Declaração de dicionários e listas
    dados = { 'Nome':str(input('\nDigite o nome: ')) , 'QDP':int(input('Quantidade de partidas: ')) , 'QG':[]}

    #fica perguntando quantos gols o jogador fez em uma partida 
    if dados['QDP'] != 0:
        while True:
            contador += 1
            dados['QG'].append(int(input(f'   Digite quantos gols o {dados["Nome"]} fez na {contador}° partida: ')))
            if contador == dados['QDP']:
                break

    deseja_continuar = str(input('Deseja continuar[s/n]: '))
    if deseja_continuar == 'n':
        break

    contador = 0