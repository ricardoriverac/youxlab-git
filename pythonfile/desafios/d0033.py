numero = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: ')) 

menor = numero
if numero2<numero and numero2<numero3:
    menor = numero2
if numero3<numero and numero3<numero2:
    menor = numero3
print(f'O menor é {menor}')
maior = numero
if numero2>numero and numero2>numero3:
    maior = numero2
if numero3>numero and numero3>numero2:
    maior = numero3
print(f'O maior é {maior}')