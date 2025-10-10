numero = list()
numeroPar = list()
numeroImpar = list()
while True:
    numero.append(int(input('Digite um número:')))
    resposta = str(input('Você quer continuar? [S/N]? '))
    if resposta in 'Nn':
        break
for c, v in enumerate(numero):
    if v % 2 == 0:
        numeroPar.append(v)
    elif v % 2 == 1:
        numeroImpar.append(v)
print(f'lista: {numero} ')
print(f'Números pares: {numeroPar}')
print(f'Números ímpares: {numeroImpar}')