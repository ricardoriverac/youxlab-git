from random import randint

resultado = ' '
tentativas = 0
while True:
    print('=' * 20)
    jogador = int(input('digite um número: '))
    computador = randint(1, 11)
    escolha = ' ' 
    while escolha not in 'PI':
        escolha = str(input('par ou ímpar?[P/I] ')).strip().upper()[0]
    total = jogador + computador
    print(f'jogador: {jogador}\ncomputador: {computador}\ntotal: {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('\033[32mvocê ganhou!\033[m')
            resultado = 'G'
            tentativas += 1
        else:
            print('\033[31mvocê perdeu!\033[m')
            resultado = 'P'
    elif escolha == 'I':
        if total % 2 == 0:
            print('\033[31mvocê perdeu!\033[m')
            resultado = 'P'
        else:
            print('\033[32mvocê ganhou!\033[m')
            resultado = 'G'
            tentativas += 1
    if resultado == 'P':
        break
print(f'após {tentativas} tentativas vitoriosas!')  