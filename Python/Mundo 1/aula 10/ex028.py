import random
numeroSorteado = input('Digite um número: ')
numeroRobo = random.randint(0, 5)
if numeroRobo == numeroSorteado: 
    print('Você venceu. PARABÉNS!')
else:
    print(f'Você perdeu!\n O número certo era {numeroRobo}')

# definir a escolha do comp. e do usua.
# conferir se o usuar. ganhou ou perdeu