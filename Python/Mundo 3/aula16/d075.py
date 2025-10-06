from random import choice
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('DIgite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numero4 = int(input('Digite o quarto número: '))
lista = (numero1, numero2, numero3, numero4)
print(lista)
print(f'O número 9 aparece {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu pela primeira vez na posição: {lista.index(3)}')
else:
    print('O número 3 não está na lista!')
print('Os números pares foram: ')
for numero in lista:
    if numero % 2 == 0:
        print(numero)