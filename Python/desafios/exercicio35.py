print('-='*20)
print('Analisandor de triangulos')
print('-='*20)
r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM formar um triangulo')
else:
    print('OS seguimentos NÃO podem formar um triangulo')