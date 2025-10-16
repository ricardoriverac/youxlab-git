import random
itens = ("Pedra", "Papel", "Tesora")
computador = random.choice(itens)
print('''SUAS JOGADAS
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print(f'Você escolheu: {itens[jogador]}')
print(f'O computador escolheu: {itens,[computador]}')
if computador == jogador:
    print('EMPATE!')
elif (computador == 0 and jogador == 2) or \
     (computador == 1 and jogador == 0) or \
     (computador == 2 and jogador == 1):
    print('COMPUTADOR GANHOU!')
else:
    print('JOGADOR GANHOU!')