'''
Faça um programa que o comprimento do cateto 
oposto e do cateto adjancente de um triângulo
retângulo, calcule e mostre o comprimento da 
hipotenusa 
''' 

#Resposta 

import math

cateto_oposto = float(input('Digite o valor do cateto oposto : '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente : '))
hipotenusa = ((math.pow(cateto_adjacente,2)) + (math.pow(cateto_oposto,2)))

print(f'O valor da hipotenusa e {hipotenusa}')