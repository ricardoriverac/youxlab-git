número = int(input('Digite um número: ')) 
total = 0
for c in range(1, número + 1):
    if número % c == 0:
        print('\033[33m', end='')
        total += 1
        
    else:
        print('\033[31m', end= '')
    print('{} '.format(c), end= '') 
    print('O número {} foi divisivel {} vezes'.format(número, total))
    if total == 2:
        print('É um numero PRIMO!')
    else:
        print('Não é um número PRIMO!')