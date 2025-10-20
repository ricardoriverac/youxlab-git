n = int(input('digite um numero para celular seu fotorial: '))
c = n
f = 1
print(f'calculando {n}! =')
while c > 0:
    print(f'{c}')
    print(f' x ' if c > 1 else ' = ')
    f *= c
    c -= 1
print(f'{f}')
