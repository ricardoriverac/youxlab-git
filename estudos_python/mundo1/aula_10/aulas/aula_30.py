'''Crie um programa que leia um número inteiro e mostre na tela se o numero e INPAR ou PAR'''

#Resposta

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O {numero} é PAR')
else :
    print (f'O {numero} é IMPAR')