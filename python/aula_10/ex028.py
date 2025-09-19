import random
numero = [0, 1, 2, 3, 4, 5]
numero_aleatorio = random.choice(numero)
print('Vou pensar em um número de 0 a 5... Tente adivinhar qual é o número!')

adivinhe = int(input('Qual é o número? '))
if adivinhe == (numero_aleatorio):
    print('VOCÊ ACERTOU, PARABÉNS!')
else:
    print('O Computador VENCEU!')