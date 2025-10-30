#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número para analisar o fatorial: '))
cont = numero
fato = 1
while cont > 0:
 print(f'{numero}', end='')
 print('x' if cont > 1 else ' = ', end='')
 fato *= cont
 cont -=1
print(f'{fato}.')