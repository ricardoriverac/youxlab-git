numero = list()
par = list()
impar = list()
while True:
    numero.append(int(input('Coloque um número:')))
    resposta = str(input('Quer continuar? [S/N]? '))
    if resposta in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista é {numero} ')
print(f'Os números pares são {par}')
print(f'Os números ímpares são {impar}')