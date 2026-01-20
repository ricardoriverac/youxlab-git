'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
em uma lista única que mantenha separados os valores pares e ímpares. No final, 
mostre os valores pares e ímpares em ordem crescente.
'''

#Resposta

dados = [[] , []]
contador = 0

for c in range(0, 7):
    contador += 1
    numero = int(input(f'Digite o {contador}° número: '))

    if numero % 2 == 0:
        dados[0].append(numero)
    else:
        dados[-1].append(numero)
dados.sort(reverse=True)
print(f'A lista dos números PARES: {dados[0]}')
print(f'A lista do números IMPARES: {dados[-1]}')
