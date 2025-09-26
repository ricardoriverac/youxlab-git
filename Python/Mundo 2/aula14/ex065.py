numero = 1
contadorMedia = 0
numeroMedia = 0
continuar = 's'
while continuar != 'n':
    numero = int(input('Digite um numero: '))
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    contadorMedia += 1
    
    numeroMedia = numeroMedia + numero 
   
    media = numeroMedia / contadorMedia
    if contadorMedia == 1:
        maior = menor  = numero
        # print(f'O numero maior é {numero}.')
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    # continuar  = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print(f'Você digitou {contadorMedia} vezes e a média é {media}.')
print(f'O maior número é {maior} e o menor número é {menor}.')


