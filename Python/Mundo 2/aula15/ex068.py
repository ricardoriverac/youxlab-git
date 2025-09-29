from random import randint
contador = 0
while True:
    opcao = int(input('Escolha uma das opções: \n[1] IMPAR\n[2] PAR\n'))
    while (opcao != 1 and opcao != 2):
        print('Você digitou errado, tente novamente!')
        opcao = int(input('Escolha uma das opções: \n[1] IMPAR\n[2] PAR\n'))
    jogo = randint(1, 2)
    if opcao != jogo:
        break
    contador += 1
    print('VOCÊ ACERTOU PARABÉNS!!!')
print('VOCÊ PERDEU!')
print(f'Você ganhou {contador} vezes consecutivas.')








    # if numero != 2:
    #         break
    # if numero != 4:
    #      break
    # if numero != 6:
    #      break
    # if numero != 8:
    #      break
    # for contador in range()