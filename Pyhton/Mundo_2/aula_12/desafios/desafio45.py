from random import randint
opcoes = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
print('Vamos jogar JO KEN PO!')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
player = int(input('Qual opção você escolhe? '))
print(f'O computador escolheu {opcoes[pc]}')
print(f'O jogador escolheu {opcoes[player]}')
if pc == 0:
    if player == 0:
        print('Empatou!')
    elif player == 1:
        print('Jogador ganha!')
    elif player == 2:
        print('computador ganha!')
    else:
        print('Não foi válido!')
elif pc == 1:
            if player == 0:
                print('computador venceu!')
            elif player == 1:
                print('empatou!')                
            elif player == 2:
                 print('jogador ganha!')
            else:
                 print('Nâo foi válido!')
elif pc == 2:
     if player == 0:
          print('Jogador ganha!')
     elif player == 1:
          print('Computador ganha!')
     elif player == 2:
          print('Empatou!')
     else:
          print('Nâo foi válido!')