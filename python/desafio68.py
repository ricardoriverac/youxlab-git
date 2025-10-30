from random import randint

vitorias = 0

print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)

    if (tipo == 'P' and total % 2 == 0) or (tipo == 'I' and total % 2 == 1):
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
        print('-' * 30)
    else:
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')

