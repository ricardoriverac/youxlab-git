from random import randint
computador = randint(0, 10)
print('sou seu computador... acabei de pensar em um numero entre 0 e 10.')
print('sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual e seu palpite?'))
    palpites += 1
    if jogador == computador:
      acertou = True
    else:
       if jogador < computador:
          print('mais... tente novamente.')
       elif jogador > computador:
          print('menos... tente novamente.')
print('acertou com {} tente novamente. parabens!'.format(palpites))
