numeros = int(input('Digite o primeiro valor:'))
int(input('Digite o segundo valor:'))
int(input('Digite o terceiro valor:'))
int(input('Digite o quarto valor:'))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print('O valor 3 apareceu na {numeros.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
    print(n, end='')