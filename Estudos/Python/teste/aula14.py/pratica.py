from math import sqrt, floor
num = float(input('Qual o número? '))
raiz = float(sqrt(num))
print(f'A raiz de {num:2}, é {floor(raiz):2}')

import random
num = random.randint(1,10)
print(num)

import emoji
print(emoji.emojize('Olá mundo :grinning_face:'))

frase = 'Curso em Video Python'
print(frase)
print(frase[3:12])
print(frase[:12])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.count('o'))
print(frase.count('O'))
frase= '   Curso em Video Python   '
print(len(frase))
print(len(frase.strip()))
frase.replace('Python', 'Android')
frase= frase.replace('Python', 'Android')
print(frase)