temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    continuar = str(input('Quer continuar?[S/N] '))
    if continuar in 'Nn':
        break
print(f'Os dados foram {principal}')
print(f'{len(principal)} pessoas foram cadastradas ao todo')
print(f'o maior peso foi de {maior}Kg e pertence à ', end= '')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor}Kg e pertence à ', end= '')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]')