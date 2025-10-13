from random import randint

vitorias = 0

while True:
    print('-=' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 30)


    numero = int(input('Digite um número:'))
    escolha = ''

    while escolha not in 'PI':
        escolha = str(input('Par ou Ìmpar?[P/I]:')).strip().upper()

    computador = randint(0,10)
    total = numero + computador
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print(f'Você jogou {numero} e o computador {computador}. Total de {total}', end=' ') 

    if (total % 2 == 0 and escolha == 'P') or (total % 2 != 0 and escolha == 'I'):
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
   
    else:
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {vitorias} vez(es).')

