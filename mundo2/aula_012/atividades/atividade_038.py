'''
Escrava um programa que leia dois números inteiros a compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
'''

#Resposta

primeiro_valor = int(input('Digite o 1° número: '))
segundo_valor = int(input('Digite o 2° número: '))

if primeiro_valor > segundo_valor :
    print('o PRIMEIRO valor e maior!!')

elif primeiro_valor < segundo_valor :
    print('O SEGUNDO valor e maior!!')

elif primeiro_valor == segundo_valor :
    print('os DOIS valores são iguais!!')