num = int(input('digite um numero: '))
for c in range(1, num + 1):
    print('{} '.format(c),end='')
#......................................
num = int(input('digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(c),end='')
    #..............................
    num = int(input('digite um numero: '))
    tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c),end='')
    print('\n\033[m0 o numeroo {} foi divisivel{} vezes'.format(num, tot))


