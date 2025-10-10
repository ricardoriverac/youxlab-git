#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo escolhido: '))
angulo_radian = math.radians(angulo)
sen = math.sin(angulo_radian)
coss = math.cos(angulo_radian)
tan = math.tan(angulo_radian)
print('O ângulo {:.4f}º  tem: '.format(angulo))
print('Seno: {:.4f}'.format(sen))
print('Cosseno: {:.4f}'.format(coss))
print('Tangente: {:.2f}'.format(tan))