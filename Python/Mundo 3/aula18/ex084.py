# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    
    pessoas.append(dados[:])  
    dados.clear()             
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 30)
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')

print(f'B) O maior peso foi de {maior_peso}Kg. Peso de ', end='') # end=' ----> serve para colocar a próxima frase na frente 
# ex.: print("Olá", end='') Olá
# ex.: print("Mundo") Mundo
# ex.: resposta ---> OláMundo

for p in pessoas:         
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()

print(f'C) O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()