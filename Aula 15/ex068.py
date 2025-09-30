from random import randint 
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'O computador jogou {computador} e você jogou {jogador}. No total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU!' )
    else:
        print('VOCÊ PERDEU!' )
        break
    elif tipo == 'I':
    if total 





