#leia o cat oposto e adjacente de um triângulo retângulo de calcule a hipotenusa

from math import pow, sqrt

catop = float(input('Digite o cat op: '))
catad = float(input('Digite o cat ad: '))
print('Cat op: {}\nCat ad: {}\nHip: {}'.format(catop,catad,sqrt(pow(catop, 2)+pow(catad, 2))))
