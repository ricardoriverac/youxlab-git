from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que vocẽ deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

'''Com Biblíoteca math'''
'''import math 
angulo = float(input('Digite o ângulo que vocẽ deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))'''

'''Vídeo de Exercício: https://youtu.be/9GvsphwW26k?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6'''