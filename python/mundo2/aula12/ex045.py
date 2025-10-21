#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('Bem-vindo ao jogo jokenpô.\n' +
      'Escolha uma opção:\n' +
      '[0] Pedra\n'+
      '[1] Papel\n'+
      '[2] Tesoura')
escolha = int(input('--> '))
if escolha == 0:
    if computador == 0:
        resultado = 'Empatou'
    elif computador == 1:
        resultado = 'Perdeu'
    else:
        resultado = 'Venceu'
    print(f'{resultado}! Você escolheu {opcoes[escolha]} e o computador escolheu {opcoes[computador]}')
elif escolha == 1:
    if computador == 0:
        resultado = 'Venceu'
    elif computador == 1:
        resultado = 'Empatou'
    else:
        resultado = 'Perdeu'
    print(f'{resultado}! Você escolheu {opcoes[escolha]} e o computador escolheu {opcoes[computador]}')
elif escolha == 2:
    if computador == 0:
        resultado = 'Perdeu'
    elif computador == 1:
        resultado = 'Venceu'
    else:
        resultado = 'Empatou'
    print(f'{resultado}! Você escolheu {opcoes[escolha]} e o computador escolheu {opcoes[computador]}')
else:
    print('Erro, opção inválida.')

