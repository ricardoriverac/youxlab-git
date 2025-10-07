import random
derrota= 'VOCÊ PERDEU!! '
vitoria=0
ParImpar = ['P', 'I']
while True:
    valor= int(input('Escolha um valor: '))
    jogador= str(input('Par ou ímpar?: [P/I] ')).upper()
    if jogador not in 'PI':
        print(str('COMECE TUDO DENOVO! '))
    computador= random.choice(ParImpar)
    computador2= random.randint(1, 10+1)
    if valor % 2 == 0:
        if computador == 'I' and jogador == 'P':
            print(f'Você escolheu {valor} e o computador escolheu {computador2}!')
            vitoria+=1
            print('Você venceu! Vamos jogar novamente... ')
        elif computador == 'P' and jogador == 'I':
            print(f'Você escolheu {valor} e o computador escolheu {computador2}!') 
            print(f'GAME OVER! Você perdeu com {vitoria} vitorias!')
    if valor % 2 != 0:
        if computador == 'P' and jogador == 'I':
            print(f'Você escolheu {valor} e o computador escolheu {computador2}!') 
            vitoria+=1
            print('Você venceu! Vamos jogar novamente... ')
        elif computador == 'I' and jogador == 'P':
            print(f'Você escolheu {valor} e o computador escolheu {computador2}!')
            print(f'GAME OVER! Você perdeu com {vitoria} vitorias!')
