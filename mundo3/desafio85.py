numeros = [[ ], [ ]]
for n in range(1, 8):
    valor = int(input(f'Digite o {n}o. valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)
print('='*50)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}\n'
      f'Os valores ímpares digitados foram: {sorted(numeros[1])}')

