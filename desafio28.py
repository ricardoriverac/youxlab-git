import random
numeros = [0,1,2,3,4,5]
resultado = random.choice(numeros)
print('Pensarei em um número de 0 a 5... Tente adivinhar!')
adivinhe = int(input('Escolhe um número: '))
if adivinhe == (resultado):
    print('Você acertou, parabéns!')
else:
    print('Eu venci! boa sorte na próxima hahaha!')