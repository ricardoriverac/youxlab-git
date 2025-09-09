import random
numero = random.randint (0, 5)
usuario = int(input('Digite um numero e veja se voce ganho ou nao: '))
if usuario == numero:
    print(f'Voce acertou \nO número era: {numero}')
else:
    print(f'Voce errou, seu estupido! \nO número era: {numero}')