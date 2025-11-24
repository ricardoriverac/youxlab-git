#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

mnh_list_pessoas = []
continu = 'S'
while continu == 'S':
   nome = input('Nome: ')
   peso = float(input('Peso: '))
   mnh_list_pessoas.append([nome, peso])
   continu = input('Você deseja cadastrar mais pessoas?[S/N]').upper()
print(f'{len(mnh_list_pessoas)} pessoas foram cadastradas.')
maior = mnh_list_pessoas[0][1]
menor = mnh_list_pessoas[0][1]
for p in mnh_list_pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]
print(f'O maior peso foi {maior} Kg. Peso de ', end='')
for p in mnh_list_pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi {menor} Kg. Peso de ', end='')
for p in mnh_list_pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
