from random import randint
number = randint(0, 5)
user = int(input('Digite qualquer número: '))
print('Você acertou!!!' if user == number else f'Ahhh, não! Você errou... \nO número era {number}')