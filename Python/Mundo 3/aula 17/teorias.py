numeros = [2, 5, 9, 1]
numeros[2] = 3
numeros.append(7)
numeros.sort(reverse=True)
numeros.insert(2, 2)
if 0 in numeros:
    numeros.remove(0)
else:
    print('Não achei o número 0')
print(numeros)
print(f'Essa lista tem {len(numeros)} elementos.')

print('-'*40)
print('   TEORIAS (pt.2)  ')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-'*40)
print('     TEORIAS (pt.3)      ')

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

print('-'*40)
print('     TEORIAS (pt. 4)     ')

a = [2, 5, 7, 3]
b = a[:]
b[2] =8
print(f'Lista A: {a}')
print(f'Lista B: {b}')