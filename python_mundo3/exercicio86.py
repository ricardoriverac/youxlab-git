valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valorp = 0
valor3 = 0
mvalor = 0

for l in range (0, 3):
    for c in range (0, 3):
        valores[l] [c] = int(input(f'Digite um número [{l}, {c}]: '))
        if valores[l] [c] % 2 == 0:
            valorp = valorp + valores[l][c]
        if valores[l][c] == valores[2][c]:
            valor3 = valor3 + valores[2][c]
        if valores[l][c] == valores[1][0]:
            mvalor = valores[1][0]
        if valores[1][1] > mvalor:
            mvalor = valores[1][1]
        if valores[1][2] > mvalor:
            mvalor = valores[1][2]

print (f'[{valores[0][0]:^4}] [{valores[0][1]:^4}] [{valores[0][2]:^4}]')
print (f'[{valores[1][0]:^4}] [{valores[1][1]:^4}] [{valores[1][2]:^4}]')
print (f'[{valores[2][0]:^4}] [{valores[2][1]:^4}] [{valores[2][2]:^4}]')
print (f'')
print (f'A soma de todos os pares é {valorp}')
print (f'A soma de todos os números da terceira coluna é {valor3}')
print (f'O maior valor da segunda coluna é {mvalor}')