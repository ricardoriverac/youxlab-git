'''lista = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    resp = ' '
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    while resp not in 'SN':
        resp = str(input('QUer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print(lista)
print(par)
print(impar)''' 
num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(num)
print(par)
print(impar)