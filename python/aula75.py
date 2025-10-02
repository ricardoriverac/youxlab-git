
num1 = int(input('digite um numero: '))
num2 = int(input('digite um numero: '))
num3 = int(input('digite um numero: '))
num4 = int(input('digite um numero: '))
numeros = (num1,num2,num3,num4)
print(f'o valor 9 aparece {(numeros.count(9))} vezes')
if 3 in numeros:
    print(f'o valor 3 aparece {numeros.index(3)}')
else:
    print('Não há valor 3.')
count = 0
for c in numeros:
    if c % 2 == 0:
        count += 1
        print(f'os numeros pares sao {c}')
   
