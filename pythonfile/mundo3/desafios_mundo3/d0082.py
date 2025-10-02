lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um numeros: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    resposta = input('Quer continuar? [S/N]').upper()
    if resposta == 'N':
        break
print(f'A lista inteira é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')