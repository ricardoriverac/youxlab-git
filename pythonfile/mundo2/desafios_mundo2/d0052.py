numero = int(input('Digite  um numero'))
total = 0
for c in range(1,numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[m0 número {numero} foi divisivel {total} vezes')
if total == 2:
    print('ele é primo')
else:
    print('ele não é primo')