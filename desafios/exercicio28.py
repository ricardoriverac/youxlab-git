import random
numero = random.randint (0, 5)
usuario = int(input('Digite um numero entre 0 a 5: '))
if usuario == numero:
    print (f'Voce acertou! {numero}')
else:
    print (f'Voce errou o numero era. {numero}')