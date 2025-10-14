from random import randint
tot = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
num = randint(0,10)
p = int(input('Qual o seu palpite?'))
while p != num:
    tot += 1
    if p < num:
        print('Mais... Tente mais uma vez')
        p = int(input('Qual o seu palpite?'))
    elif p > num:
        print('Menos... Tente mais uma vez')
        p = int(input('Qual o seu palpite?'))
print(f'Acertou com {tot} tentativa(s). Parabéns!')