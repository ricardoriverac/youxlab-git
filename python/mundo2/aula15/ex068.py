#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
vai_jogar = "s"
vitoria_consecutivas = 0
while vai_jogar == "s":
    opcao = input('Digite se você deseja jogar par ou ímpar?[I/P]').lower()
    escolha = int(input('Digite qual número você deseja jogar: '))
    computador = random.randint(0,10)
    print(f'Computador jogou {computador} e o jogador {escolha}')
    soma = escolha + computador
    if soma % 2 == 0:
        if opcao == 'p':
            print('Você venceu.')
            vitoria_consecutivas += 1
            print(f'Você ganhou {vitoria_consecutivas} consecutivas.')
        else:
            print('Você perdeu.')
    else:
        if opcao == 'i':
            print('Você venceu.')
            vitoria_consecutivas += 1
            print(f'Você ganhou {vitoria_consecutivas} consecutivas.')
        else:
         print('Você perdeu.')
    vai_jogar = input('Você deseja continuar? [S/N]').lower()


