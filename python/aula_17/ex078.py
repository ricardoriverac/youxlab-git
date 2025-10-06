'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''

lista = list()
for valores in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os numeros digitados foram: {lista}')
print(f'O maior valor foi {max(lista)} na posição ', end='')
for int, v in enumerate(lista):
    if max(lista) == v:
        print(f'{int}', end='ª ')
print()
print(f'O menor valor foi {min(lista)} na posição ', end='')
for int, v in enumerate(lista):
    if min(lista) == v:
        print(f'{int}', end='ª ')

