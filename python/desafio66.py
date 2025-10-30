ds44soma = 0
contador = 0
maior = None
menor = None
while True:
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
media = soma / contador
print(f'\nVocê digitou {contador} números.')
print(f'A média dos valores digitados é {media:.2f}.')
print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')
