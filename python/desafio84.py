temp = []
pessoas = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])  # adiciona uma cópia da lista temp
    temp.clear()  # limpa para a próxima entrada
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'B) O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'C) O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
