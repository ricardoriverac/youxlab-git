'''Cria um programa que leia o nome completo de uma pessoa a mostre:

O nome com todas as letras maiúsculas

O nome com todas minúsculas.

Quantas letras ao todo (sem considerar espaços).

Quantas letras tem o primeiro nome.'''

#Resposta

digite_nome = input('Digite o seu nome: ')

nome_maiusculo = ((digite_nome).upper())

nome_minusculo = ((digite_nome).lower())

n = (' '.join(digite_nome))
n2 = (n.split())
contagemdeletras = (len(n2))

n3 = (digite_nome.split())
contagemdoprimeironome = (len(n3[0]))

print(f'\nO seu nome em maiusculo: {nome_maiusculo}')
print(f'O seu nome em minusculo: {nome_minusculo}')
print(f'A quantidade de letras que seu nome completo tem: {contagemdeletras}')
print(f'A quantidade de letras do seu primeiro nome: {contagemdoprimeironome}')