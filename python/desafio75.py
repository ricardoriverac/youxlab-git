numeros = (
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')),
    int(input('Digite o 4º número: '))
)

print(f'\nVocê digitou os valores: {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')

if 3 in numeros:
    print(f'O valor 3 apareceu primeiro na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

print('Os números pares digitados foram: ', end='')
pares = 0
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
        pares += 1
if pares == 0:
    print('Nenhum número par foi digitado.')
