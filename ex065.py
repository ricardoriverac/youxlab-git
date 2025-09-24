numero = 0
media = 0 
soma = 0
count = 0 
menor = 10000
maior = 0
continuar = 'S'
while continuar == 'S':
    numero= int(input('Digite um numero'))
    count += 1
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero 
    continuar = input('Deseja continuar(S/N)?').upper()
media = (soma/count)
print(f'A media entre os valores é de {media} e o maior valor é {maior} e o menor é {menor}')

