#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
   area_terreno = largura * comprimento
   print(f'A área do terreno é: {area_terreno} metros quadrados.')
largura_terreno = 20.5
comprimento_terreno = 50.0
area(largura_terreno, comprimento_terreno)
