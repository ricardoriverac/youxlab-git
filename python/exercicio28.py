import random 
resposta = int(input('escolha um número de 1 a 5: '))
numero = [1, 2, 3, 4, 5]
escolhido = random.choice(numero)
if resposta == escolhido:
    print ('parabéns, você acertou o número escolhido pelo computador')
else:
    print ('você errou o número :( tente novemente, o número escolhido era {}' .format(escolhido))