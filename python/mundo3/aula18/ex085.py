#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []
for u in range(0,7):
    user = int(input('Digite um valor: '))
    lista.append(user)
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
print(f'Lista completa: {lista}')
print(f'Lista dos números pares em ordem crescente: {par}')
print(f'Lista dos números ímpares em ordem crescente: {impar} ')