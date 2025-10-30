#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

valor1 = 0
valor2 = 1
termos = int(input('Escolha a quantidade de termos: '))
print(f'{valor1} > {valor2} > ', end=' ')
while termos > 2:
    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3
    termos -= 1
    print(f'{valor3}', end=' > ')
print('Fim')