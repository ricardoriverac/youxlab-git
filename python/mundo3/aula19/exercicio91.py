import random
jogadores={}
maiorValor={}
numeros=[jogadores]

print('Escolha ')
jogadores['jogador1'] = random.randint(0,6)
jogadores['jogador2'] = random.randint(0,6) 
jogadores['jogador3'] = random.randint(0,6)
jogadores['jogador4'] = random.randint(0,6)

for n,v in jogadores.items():
    print(f'{n} tirou {v}')
maiorJogador=max(jogadores)
numeros.sort(reverse=True)

max(jogadores.values())

print(numeros)



# Ordenar por valores (decrescente)
dicionario_ordenado_valores_desc = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

lista_chaves=list(dicionario_ordenado_valores_desc.keys())
chaveDoMaiorValor=lista_chaves[0]


print(f'O jogador com maior valor foi {chaveDoMaiorValor}')

for c,v in dicionario_ordenado_valores_desc.items():
    print(f'{c}:{v}')
