valores = [[], []]
print('-'*20)

for c in range(7):
    numero = int(input('-> ''Digite um valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
print('-'*20)
print(f'-Os números pares foram: {sorted(valores[0])}.\n-Os números ímpares foram: {sorted(valores[1])}.')