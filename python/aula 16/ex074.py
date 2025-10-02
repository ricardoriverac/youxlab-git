from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10), randint(1,10))
print('O valor sorteado foiiii: ', end='')
for num in numero: 
    print(f'{num} ', end='')
print(f'O numero maior sorteado foi {max(numero)}')
print(f'O numero menor sorteado foi {min(numero)}') 