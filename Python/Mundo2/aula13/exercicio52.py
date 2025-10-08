num_inteiro = int(input('Digite um numero inteiro: '))
tot = 0 
for c in range(1, num_inteiro + 1 ):
    if num_inteiro % c == 0:
        print('\033[33', end='')
        tot += 1
    else:
        print('\033[31', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 numero {} foi divisivel por {} vezes'.format(num_inteiro, tot))
if tot == 2:
    print('E por isso ele e PRIMO!')
else:
    print("E por isso ele não e PRIMO!")