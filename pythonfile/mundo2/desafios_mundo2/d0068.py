from random import randint
computador = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador  
    opcoes = 'PI'
    opcoes = str(input('Você quer par ou impar [P/I]: '))
    print(f'Você escolheu {jogador} e o computador jogou {computador}. O resultado foi {soma}')
    if  opcoes == 'Pp' or 'Ii':
        if soma %2 == 0:
            print('Você ganhou')
        else:
            print('Você perdeu')
            break