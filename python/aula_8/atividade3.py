import math
angulo = float(input("digite o angulo que vocễ deseja: "))
seno = math.sin(math.radians(angulo))
print (f"O angulo de {angulo} tem o seno de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem o tangente de {tangente:.2f}")