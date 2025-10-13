numero = []
contador = 0
soma = 0 

while True:

    primeiroNumero = int(input('Digite um número:'))
    contador += 1
    soma += primeiroNumero
    numero.append(primeiroNumero)
    continuar = str(input('Quer continuar[S/N]?:'))
    if continuar.upper() == 'N':
       print('Muito obrigado por usar meu programa volte sempre :)')
       break


if numero:
    media = (soma/len(numero))
    maior = max(numero)
    menor = min(numero)



print('Você digitou {} números e a média foi de {:.2f}'.format(contador,media))
print('O menor número digitado foi {}'.format(menor))

