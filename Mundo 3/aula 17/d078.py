valores = []
maiorNumero = 0
menorNumero = 999999
for quantia in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    for valor in valores:
        if valor < menorNumero:
            menorNumero = valor
        if valor > maiorNumero:
            maiorNumero = valor
for v, pos in enumerate (valores):
    print(f'O número {pos} está na posição {v}')
print(f'Lista: {valores}')
print(f'O MAIOR número é: {maiorNumero}.')
print(f'O MENOR número é: {menorNumero}') 