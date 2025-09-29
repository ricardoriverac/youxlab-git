continuar = 's'
n = int(input('Digite o número: '))
soma = maior = menor = n
continuar = str(input('Novo número [s/n]? ')).lower().strip()[0]
cont = 1
while continuar == 's':
    n = int(input('Digite o número: '))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    else:
        menor = n
    continuar = str(input('Novo número [s/n]? ')).lower().strip()[0]
menor = menor
media = soma / cont
print(f'Você digitou {cont} números. A média deles é {media}')
print(f'O maior número foi {maior}, o menor número foi {menor}')