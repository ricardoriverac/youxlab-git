'''
Escreva um programa que leia um número n inteiro qualquer e mostra na tela
os n primeiros elementos de uma Sequência de Fibonacci.
Ex:
0-1-1-2-3-5-8
'''

#Resposta

elementos_fibonacci = int(input('''Digite a quantidade de elementos de uma Sequência de Fibonacci: '''))
repeticao = 2
fibonacci1 = 0
fibonacci2 = 1
print(f'{fibonacci1} + {fibonacci2} ', end= '+ ')
while repeticao != elementos_fibonacci :
    repeticao += 1

    fibonacci3 = fibonacci1 + fibonacci2 
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3
    print(f'{fibonacci3}', end= ' + ')

