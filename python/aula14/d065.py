resposta = 'S'
soma = 0
quantidade = 0
media = 0
maior = 0
menor = 999999
while resposta in 'Ss':
    numero = int(input('Digite um valor: '))
    soma += numero 
    quantidade += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    resposta = str(input('Você deseja continuar a digitar valores? [S/N] '))
media =  soma / quantidade
print(f'A média entre todos os números é igual a {media}')
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')