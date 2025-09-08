from math import radians, sin, cos, tan
ângulo = float(input('digite o ângulo que vocẽ deseja: '))
seno = sin(radians(ângulo))
print(' o angulo de {} tem SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('o ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))