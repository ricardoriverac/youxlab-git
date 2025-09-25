n = int(input('Digite um número para calcular seu FATORIAL: '))
c = n
f = 1
print(f'CALCULANDO -> {n}! = ', end = ' ')
while c > 0:
    print(f'{c}', end = ' ')
    print(' x ' if c > 1 else ' = ', end = ' ')
    f *= c
    c -= 1
print(f'{f}')