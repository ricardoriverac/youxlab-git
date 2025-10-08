numero = 1

while numero != 0:
    numero = int(input('De qual número deseja ver a tabuada: '))
    if numero < 0:
        break
    else:
        print('-' * 25)
        print(f'{numero} x {0} = {numero * 0}')
        print(f'{numero} x {1} = {numero * 1}')
        print(f'{numero} x {2} = {numero * 2}')
        print(f'{numero} x {3} = {numero * 3}')
        print(f'{numero} x {4} = {numero * 4}')
        print(f'{numero} x {5} = {numero * 5}')
        print(f'{numero} x {6} = {numero * 6}')
        print(f'{numero} x {7} = {numero * 7}')
        print(f'{numero} x {8} = {numero * 8}')
        print(f'{numero} x {9} = {numero * 9}')
        print('-' * 25)

print('-' * 25)
print('Programa encerrado. Volte sempre!')