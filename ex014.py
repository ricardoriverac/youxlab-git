import math
angulo=float(input('digite o ângulo que você deseja: '))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print('o ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('o ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))