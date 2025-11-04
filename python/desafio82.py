numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
