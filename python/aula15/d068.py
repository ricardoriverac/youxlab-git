from random import choice
lista = ['impar', 'par']
jogador = str(input('Escolha entre PAR ou ÍMPAR: '))
computador = choice(lista)
contador = 0
while jogador == computador:
    contador += 1
    print('ACERTOU!')
    jogador = str(input('Escolha novamente entre PAR ou IMPAR: '))
    computador = choice(lista)
print(f'Você ERROU!')
print(f'Você ACERTOU {contador} consecutivas!')
print('=' * 20)

        