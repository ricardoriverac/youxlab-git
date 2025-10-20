listaUsuario = [[], []]
numeros = 0
for i in range(1, 8):
    numeros = int(input(f'digite o {i}o. numeros: '))
    if numeros % 2 == 0:
        listaUsuario[0].append(numeros)
    else:
        listaUsuario[1].append(numeros)
    listaUsuario[0].sort()
    listaUsuario[1].sort
    print(f'o valor pares sao: {listaUsuario[0]}')
    print(f'o valor impares sao: {listaUsuario[1]}')
    