#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adajcente: '))
hipotenusa = math.sqrt (cateto_oposto**2 + cateto_adjacente**2)
print('O comprimento da hipotenusa é: {:.3f}'.format(hipotenusa))






