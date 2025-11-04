numeros = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Você digitou {len(numeros)} números.')
print(f'B) Os valores em ordem decrescente são {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('C) O valor 5 foi digitado e está na lista.')
else:
    print('C) O valor 5 não foi digitado na lista.')
