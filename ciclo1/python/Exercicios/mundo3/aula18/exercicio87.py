matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = soma_2 = 0

for i in range(0, 3):
    for c in range(0, 3):
        matriz [i][c] = int(input(f"Digitę um valor para [{1}, {c}]: "))

for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz [i] [c]:^5}]", end='')
        if matriz [i] [c] % 2 == 0:
            soma += matriz [i] [c]

print() 
print(f'A soma dos valores pares é {soma}') 
for i in range(0, 3): 
    soma_2 += matriz [1] [2]
print(f'A soma dos valores da terceira coluna é {soma_2}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1] [c]
    elif matriz[1] [c] > maior:
        maior = matriz [1] [c]
print(f"maior valor da segunda Linha é {maior}.")