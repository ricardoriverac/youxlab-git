# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
#  que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    largura = float(input('largura (m): '))
    comprimento = float(input('comprimento (m): '))
    area = largura * comprimento
    print(f'A área do terreno  é de {largura} de largura e {comprimento} de comprimento é de {area}m².')
print('Controle de Terrenos')
area()