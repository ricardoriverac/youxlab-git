from random import randint

while True:
    jogador = int(input('Digite o valor desejado: '))
    computador = randint(0,10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]\n')).strip().upper()[0]
    print(f'Você jogou {jogador}\nO computador jogou {computador}\nA soma deu {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Ganhou')
        else:
            print('Perdeu')
            break
    elif tipo == 'I':
        if soma % 2 != 0:
            print('Ganhou')
        else: 
            print('Perdeu')
            break