from math import radians, sin, cos, tan
ângulo = float(input('escreva o angulo que você'))
seno = sin (radians(ângulo))
print(f' O âgulo de {ângulo} tem o seno de {seno}')
cosseno = cos(radians(ângulo))
print(f'O ângulode {ângulo} tem o cosseno de {cosseno}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o tangente de {tangente}')
