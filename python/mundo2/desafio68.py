from random import randint


b=30
JOGADAS=0
fim=''
while True:
    if fim == 'fim':
        break
    else:
        print('=-' * b)
        print('VAMOS JOGRA PAR OU IMPAR')
        print('=-' * b)
        sair = 1
        escolha = ''
        num = randint (0, 100)
        jogador=(input('Digite um Valor1 :'))
        vazio=bool(jogador)
        numero=(jogador.isnumeric())
        if vazio == True and numero == True:
            jogador = int(jogador)
            while sair != 0:
                escolha = str(input('PAR OU IMPAR? [P/I]')).upper()
                print('=-' * b)
                if escolha == 'P':
                    resultado=(jogador+num) % 2
                    if resultado==0:
                        JOGADAS=JOGADAS+1
                        print(f'Resultado da Partida Play {JOGADAS} X CUP 0 ')
                        sair=0
                    else:
                        print(f'Voce pediu [PAR] escolheu o numero {jogador} e o computador {num}.somado os dois {jogador+num} que igual Impar ')
                        fim='fim'
                        sair = 0
                elif escolha == 'I':
                    resultado = (jogador + num) % 2
                    if resultado == 0:
                        print(f'Voce pediu [IMPAR] escolheu o numero {jogador} e o computador {num}.somado os dois {jogador + num} que igual Par ')
                        fim = 'fim'
                        sair = 0
                    else:
                       JOGADAS = JOGADAS + 1
                       print(f'Resultado da Partida Play {JOGADAS} X CUP 0 ')
                       sair = 0
                else:
                    print(f'VOCE DIGITOU A LETRA: [{escolha}] OPÇÂO INVALIDA,TENTE DINOVO')
                    sleep(1)
                    print('=-' * b)
                    sair = 1
        else:
            if vazio == False:
                print('Não podemos continuar o jogo se não digitar um numero ')
                sleep(1)
                print('=-' * b)
            elif numero==False:
                print(f'O valor digitado [{jogador}] não correspode a numero so vale  numeros')
                sleep(1)
                print('=-' * b)

print('-' *b)
print('VOCE PERDEU')
print('-' *b)
print(f'GAME OVER ! voce venceu {JOGADAS} vezes')
