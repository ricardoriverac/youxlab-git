# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
maiorPeso = menorPeso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    
    pessoas.append(dados[:])  
    dados.clear()             
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 30)
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')

print(f'B) O maior peso foi de {maiorPeso}Kg. Peso de ', end='') # end=' ----> serve para colocar a próxima frase na frente 
# ex.: print("Olá", end='') Olá
# ex.: print("Mundo") Mundo
# ex.: resposta ---> OláMundo

for p in pessoas:         
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()

print(f'C) O menor peso foi de {menorPeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
print()