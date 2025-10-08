numero = [int(input('Digite um numero: ')), 
int(input('Digite um numero: ')), 
int(input('Digite um numero: ')), 
int(input('Digite um numero:'))]
print(f'Números Digitados; {numero}')
print(f'O número 9 apareceu {numero.count(9)} vezes. ')
if 3 in numero:
    print(f'O número 3 foi digitado na posição {numero.index(3)+1}. ')
else:
    print('O número 3 não foi digitado')
print(f'Números pares: ', end='') 
for n in numero:
    if n % 2 == 0: 
        print(n, end='')