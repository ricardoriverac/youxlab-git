numero = int(input('Digite um número para calcular seu fatorial: '))
c = numero
fatorial = 1
print(f'Vamos calcular {numero}!')
while c > 0:
    print(f'{c} ', end= '' )
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c -=1
print(f'{fatorial}')


