numero = int(input('Digite o número que deseja saber se é um número primo: '))
contagem = 0
for c in range(1, numero+1):
    if numero % c == 0: 
        contagem += 1
        print('\033[32m', end=(''))
    else:
        print('\033[31m', end=(''))
    print('{} '.format(c), end=(''))

if contagem == 2:
    print(f'\n\033[mO número {numero} é um número primo.')
else:
    print(f'\n\033[mO número {numero} não é um número primo.')