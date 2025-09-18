n = int(input('digite um numero para celular seu fotorial: '))
c = nf = 1
f = 1
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
