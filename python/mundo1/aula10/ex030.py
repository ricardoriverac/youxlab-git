#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Digite um número para dizer se ele é ímpar ou par: '))
if number % 2 == 0:
    print(f'O número {number} é par.')
else:
    print(f'O número {number} é ímpar.')
