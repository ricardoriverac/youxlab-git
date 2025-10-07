from random import randint
numero = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('O número sorteado é: ', end='')
for num in numero:
    print(f'{num}', end='')
print(f'O número sorteado é: {max(numero)}')
print(f'O menor número sorteado é: {min(numero)}')