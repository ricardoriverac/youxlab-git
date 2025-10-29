numero = int(input('Indique um número para ver sua tabuada: '))
print(f'\nTabuada do {numero}:')
for i in range(11):
    print(f'{numero} x {i} = {numero * i}')
