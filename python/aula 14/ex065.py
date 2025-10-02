continuar = 's'
numero = int(input('Digite o número: '))
soma = maior = menor = numero
continuar = str(input('Novo número [s/n]? ')).lower().strip()[0]
conta = 1
while continuar == 's':
    numero = int(input('Digite o número: '))
    soma += numero
    conta += 1
    if numero > maior:
        maior = numero
    else:
        menor = numero
    continuar = str(input('Novo número [s/n]? ')).lower().strip()[0]
menor = menor
media = soma / conta
print(f'Você digitou {conta} números. A média deles é {media}')
print(f'O maior número foi {maior}, o menor número foi {menor}')