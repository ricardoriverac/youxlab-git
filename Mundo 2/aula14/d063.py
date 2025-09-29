numero = int(input('Quantos números quer que apareça: '))
termo1 = 0
termo2 = 1
print(f'{termo1} -> {termo2}', end=' ')
contar = 3
while contar <= numero:
    termo3 = termo1 + termo2
    print(f'-> {termo3}', end=' ' )
    termo1 = termo2
    termo2 = termo3
    contar += 1
print('FIM') 