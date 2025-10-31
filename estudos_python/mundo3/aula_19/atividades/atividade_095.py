'''CODIGO NÃO FINALIZADO'''

'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo 
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

#Responda

#Declaração de listas e dicionários
time = []
jogadores_gols = {}
gols = []

while True:
    #Pergunta os valores 
    nome = str(input('Digite o seu nome: '))
    quantidade_partida = int(input('Qual a quantidade de partidas jogadas: '))

    #Fica perguntanto quantos gols o jogador fez em cada partida
    for c in range(0, quantidade_partida):
        quantidade_gols = int(input(f'Qual a quantidade de gols da {c+1}° partida: '))

    #Pergunta se deseja continuar registrando jogadores
    deseja_continuar = str(input('Deseja continuar[s/n]: ')).lower()

    #Adiciona os valores nas listas
    gols.append(quantidade_gols)
    print(gols)

    #Verifica se a pessoa deseja continuar cadastrando jogadores
    if deseja_continuar == 'n':
        break
    elif deseja_continuar != 's':
        while True:
            deseja_continuar = str(input('Dados invalidos. Deseja continuar[s/n]: ')).lower()
            if deseja_continuar == 's':
                break
            elif deseja_continuar == 'n':
                break
        if deseja_continuar == 'n':
            break
