#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

mnh_list_peso = []
mnh_list_nome = []
continuar = 'S'
while continuar == 'S':
    nome = input('NOME: ')
    mnh_list_nome.append(nome)
    peso = float(input('PESO: '))
    mnh_list_peso.append(peso)
    continuar = input('Você deseja cadastrar mais pessoas:[S/N]').upper()
print(f'{len(mnh_list_nome)} pessoas foram cadastradas.')
calculo = (len()) / (peso ** 2)