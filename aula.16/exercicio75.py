num = (int(input('Digite o valor 1: ')),
       int(input('Digite o valor 2: ')),
       int(input('Digite o valor 3: ')),
       int(input('Digite o valor 4: ')))
print(f'Voce  digitou os valores: {num}')
print(f'O valor 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')   