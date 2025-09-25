import random
numeroRobo = random.randint(0, 10)
numeroPessoa = int(input('Digite o seu número da sorte: '))
contPalpites = 1
while numeroPessoa != numeroRobo:
    print('Você errou! tente novamente!')
    numeroPessoa = int(input('Digite o seu número da sorte: '))
    contPalpites += 1
print(f'Você acertou parabéns!\nSua quantidades de palpites foi {contPalpites} vezes.')
#     print('Você venceu. PARABÉNS!')
# else:
#     print(f'Você perdeu!\n O número certo era {numeroRobo}')