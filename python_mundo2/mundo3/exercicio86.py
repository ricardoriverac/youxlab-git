valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range (0, 3):
        valores[l] [c] = int(input(f'Digite um número [{l}, {c}]: '))
print (f'[{valores[0][0]}] [{valores[0][1]}] [{valores[0][2]}]')
print (f'[{valores[1][0]}] [{valores[1][1]}] [{valores[1][2]}]')
print (f'[{valores[2][0]}] [{valores[2][1]}] [{valores[2][2]}]')