matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('-'*25)
print('    INICIANDO PROGRAMA   ')
print('-'*25)
for l in range(0, 3):
    for f in range(0, 3):
        matriz[l][f] = int(input(f'-''Número para a sua matriz [{l}, {f}]: '))
print('-'*25)
for l in range(0, 3):
    for f in range(0, 3):
        print(f'[{matriz[l][f]}]', end='')
    print()