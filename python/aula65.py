resp = 's'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('digite um numero'))
    soma += num
    #soma = soma + num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar? [S/N] ')).upper().split()[0]
media = soma / quant
print('voce digitou {} numeros e a media foi {}'.format(quant, media))
print('o maior valor foi {} e o menor valor foi {}' .format(maior, menor))