import random
numero = int(input('Adivinhe qual número foi escolhido: '))
numero_inteiro = random.randint(0, 5)
print(numero_inteiro)
if numero == numero_inteiro:
    print('Você GANHOU!')
else:
    print('Você PERDEU!')



