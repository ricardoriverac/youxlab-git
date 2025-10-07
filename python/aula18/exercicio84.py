pessoa = []
galera = []
answer = ' '
maior = menor = 0
while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite o peso: ')))
    if len(galera) == 1:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    answer = str(input('Quer continuar? [S/N] '))
    if answer not in 'Ss':
        break
    
galera.sort()
print(len(galera))
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end = ' ')
print()
for p in galera:
    if p in galera:
        if p[1] == menor:
            print(f'[{p[0]}]', end = ' ')
