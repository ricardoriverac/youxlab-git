'''
Desenvolva um programa que leia o comprimento de 
três retas a diga ao usuário se elas podem ou não 
formar um triangulo.
'''

#Resposta

a = float(input('a'))
b = float(input('b'))
c = float(input('c'))

if a + b > c and a + c > b and b + c > a:

    print('Pode formar um triângulo')

else:

    print('Não podem formar um triângulo')