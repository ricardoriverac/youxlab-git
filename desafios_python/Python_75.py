numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite outro número:'))
numero3 = int(input('Digite mais um número:'))
numero4 = int(input('Digite o último número: '))
tupla = (numero1,numero2,numero3,numero4)

print(f'Você digitou os seguintes valores: {tupla} ')
print(f'O valor 9 aparece {tupla.count(9)} vezes ')
print(f'O valor 3 aparece na {tupla.index(3)+1}ª  posição')
print(f'Os valore pares digitados foram')

for numero in tupla:
    if numero % 2 == 0:
        print(f'{numero} ',end= '')
print()
