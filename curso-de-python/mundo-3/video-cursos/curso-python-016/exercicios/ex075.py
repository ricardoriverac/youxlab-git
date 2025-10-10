numeros = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: '))) 

print(f'O número 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O número 3 aparece pela primeira vez na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O número 3 não está em nenhuma posição.')

print('Os números pares são ', end='')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')