from random import randint
while True:
    escolha = str(input('Par ou Impar: ')).lower()
    # print(escolha)
    jogador = int(input('Digite um valor: '))
    computador = randint(0,11)
    soma = jogador + computador 
    print(f'Voce escolheu {jogador} e o computador escolheu {computador} ')
    if escolha == 'par':
        if soma %2 == 0:
            print('voce ganhou')
        else:
            print('voce perdeu')
        break
    if escolha == 'impar':
        if soma %2 == 0:
            print('Voce perdeu')
        else:
            print('Voce ganhou')

    
