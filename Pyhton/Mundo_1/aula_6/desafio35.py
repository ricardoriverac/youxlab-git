r1 = float(input('Digite um número: '))
r2 = float(input('Digite outro número: '))
r3 = float(input('Digite outro número: '))
conta = r1 + r2
conta2 = r2 + r3
conta3 = r1 + r3
if r1<conta2 and r2<conta3 and r3<conta :
    print('É possível formar um triângulo!')
else:
    print('Nao é possível formar um triângulo!')