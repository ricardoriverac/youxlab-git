'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

#Resposta

#Declaração de variaveis
contador2 = contador = 0

#Declaração de dicionários e listas
dados = { 'Nome':str(input('Digite o nome: ')) , 'QDP':int(input('Quantidade de partidas: ')) , 'QG':[]}

#fica perguntando quantos gols o jogador fez em uma partida 
if dados['QDP'] != 0:
    while True:
        contador += 1
        dados['QG'].append(int(input(f'   Digite quantos gols o {dados["Nome"]} fez na {contador}° partida: ')))
        if contador == dados['QDP']:
            break

#mostra uma tabela mostrando a quantidade de gils fez em cada partida e a soma de todos os gols
print(f'\nO jogador {dados["Nome"]} fez:')
for c, v in enumerate(dados['QG']):
    contador2 += 1
    print(f'{contador2}° partida fez {v} gols. ')