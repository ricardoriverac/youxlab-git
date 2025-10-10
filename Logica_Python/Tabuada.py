numero = (input('Digite um numero para ver sua tabuada:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, numero*c))