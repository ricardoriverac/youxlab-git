from random import randint
computador = randint(0, 10)
print('Sou seu computador, pensei em um número de 0 a 10')
print('Tente advinhar!!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número MAIOR!')
        elif jogador > computador:
            print('Tente um número MENOR!')

print(f'Acertou!!! Com {palpites} palpites!')