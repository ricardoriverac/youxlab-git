numero = list()
par = list()
impar = list()
while True:
    numero.append(int(input('Insira um número: ')))
    resp = str(input('Deseja contunuar?[S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista é {numero}')
print(f'Os pares são {par}')
print(f'Os impares são {impar}')