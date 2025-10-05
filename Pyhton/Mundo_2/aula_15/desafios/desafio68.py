import random
n = 0
while True:
    opcao = int(input('Você escolhe, par(1) ou impar?(2) [1,2]'))
    pc = random.randint(1,2)
    player = int(input('Escolha um número: '))
    if opcao == 1:
        pc + player % 2 == 0
        print('Parabéns! Você ganhou!')
        n = n + 1
    else:
        print('Eu venci, fim de jogo hahaha.')
        break
    if opcao == 2:
        pc + player % 2 == 0
        print('Eu ganhei!! Fim de jogo hahaha')
        n = n + 1
    else:
        print('Parabéns, você ganhou')
        break
print(f'No total foram {n} vitórias! parabéns!')