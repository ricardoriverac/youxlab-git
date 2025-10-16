numero = [[], []]
certo = 0
for i in range(1, 8):
    certo = int(input(f'Digite o {i}. valor: '))
    if certo % 2 == 0:
        numero[0].append(certo)
    else:
        numero[1].append(certo)
print('=' * 50)
numero[0].sort()
numero[1].sort()
print(f'Os numeros pares encontrados foi: {numero[0]}')
print(f'Os numeros ímpares encontrados foi: {numero[1]}')