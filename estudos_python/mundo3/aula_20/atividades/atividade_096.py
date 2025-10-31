'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões 
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

#Responda

def area(l, c):
    r = l * c
    print(f'A área do retangulo: {r}m')


largura = float(input('Digite a largura(m): '))
comprimento = float(input('Digite o comprimento(m): '))
area(largura, comprimento)