from random import randint 
jogo = [] 
jogadores = {} 
vencedor = [] 
maiorDado = 0

for c in range (4): 
    jogadores['pessoa'] = input('Insira o nome do jogador: ') 
    jogadores['dado'] = randint(1,6) 
    jogo.append(jogadores.copy()) 
    print (jogadores) 

for p in jogo:
    if p['dado'] > maiorDado:
        vencedor.clear()
        vencedor.append(p.copy())
        maiorDado = p['dado']
    else:
        if p['dado'] == maiorDado:
            vencedor.append(p.copy())
print (f'E o vencedor/vencedores são: {vencedor}')