base = int(input('Digite um número: '))
cont = 0
for c in range(1, base+1):
    if base % c == 0:
        print(f'\033[94m{c}', end = ' ')
        cont += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {base} foi dividido {cont} vezes')

if cont == 2:
    print('\033[32mO número é PRIMO')
else:
    print('\033[31mO número NÃO é PRIMO')

#cont = 0 define um valor nulo a um objeto que será usado posteriormente
#nesse caso, o valor seria somado a cada número múltiplo de 'base' encontrado
#se cont == 2, significa que apenas 2 números são divisíveis, sendo eles o próprio número e o número 1, significa que o número é primo
#se cont > 2, significa que o número não é primo
#/033[m -> define uma cor determinada pelo número anterior ao m
