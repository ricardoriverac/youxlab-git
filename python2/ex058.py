from random import randint
computador = randint(0, 10)
print('Consegue advinhar em que numero entre 0 e 10 eu estou pensando?')
jogador = int(input('Qual é seu palpite?'))
tentativas = 1
while jogador != computador:
    if jogador < computador:
        print('Mais..Tente mais uma vez')
    else :
        print('Menos..Tente mais uma vez')
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas.PARABENS!!') 
