numeros = list()
while True:
    n = int(input('Digite algum valor:'))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado')
    r = str(input(Quer continuar? [S/N]))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')