'''
Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.
'''

from time import sleep

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(area_terreno)

print('-=' * 5, 'controle de terrenos'.upper(), '-=' *5)


largura = int(input('Qual é a largura? '))
comprimento = int(input('Qual é o comprimento? '))
print(f'Calculando a area de um terreno {largura} x {comprimento}....')

sleep(3)

print('-> RESULTADO FINAL' ) 
area(largura, comprimento)
