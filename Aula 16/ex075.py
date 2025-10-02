numeros = int(input('Digite um numero:')), int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:'))
print(f'Foram digitados os números: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes. ')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1} posição. ')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares que você digitou foram: ', end='') 

for n in numeros:
    if n % 2 == 0:
        print(n, end= ' ')
