import random
print('Pensarei em um número aleatório de 0 a 10. . . Tente acertar! ')
numero = random.choice(range(0,10))
resposta = int(input('Minha escolha é: '))
e = 1
while resposta != numero:
    print('errou hahaha! tente novamente.')
    resposta = int(input('Minha resposta então é: '))
    e = e + 1
if resposta == numero:
    print('AFF! você acertou! parabéns.')