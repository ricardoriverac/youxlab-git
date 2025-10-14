lista = [[], [], []]
pares = terceiros = maior = 0

for c in range(0, 3):
    for n in range(0, 3):
        lista[c].append(int(input(f'Digite um valor para [{c}, {n}]: ')))

print('-=-' * 30)

for cont in range(0, 3):
    for val in range(0, 3):
        print(f'[{lista[cont][val]:^5}]', end=' ')
        if lista[cont][val] % 2 == 0:
            pares += lista[cont][val]
    print()

terceiros = lista[0][2] + lista[1][2] + lista[2][2]

for valor in lista[1]:
    if valor > maior:
        maior = valor

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceiros}')
print(f'O maior valor da segundo linha é {maior}')