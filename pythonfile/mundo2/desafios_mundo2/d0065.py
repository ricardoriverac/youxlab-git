resposta = 'Ss'
soma = 0
media = 0 
contador = 0
maior = 0
menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um numero'))
    contador +=1
    soma += numero     
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Você quer continuar? [S/N]'))
media = soma / contador
print(f'Você digitu {contador} numeros')
print(f'A media dos numeros digitados foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
