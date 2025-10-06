numeros = list()
par = list()
impar = list()
while True:
    numeros.append(int(input('Digite um número por favor:')))
    resultado = str(input('Aceita continuar? [S/N]? '))
    if resultado in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista é {numeros} ')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')