'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numero = []
while True:
    numero.append(int(input('informe um valor para que possamos ler: ')))
    valor = str(input('Deseja continuar? [S/N] '))
    if valor in 'Nn':
        break
print('=' * 50)
print(f'Vc colocou {len(numero)} valores: ')
numero.sort(reverse=True)
print('Os numeros em ordem decrescente são{}'.format(numero))
if 5 in numero:
    print('O numero 5 está presente na lista ')
else: 
    print('O numero 5 não está presente na lista')