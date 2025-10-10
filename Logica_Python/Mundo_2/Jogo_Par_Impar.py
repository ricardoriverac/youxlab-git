from random import randit 

while True:
    jogador = int(input('Diga um valor: '))
    computador = randit(0, 11)
    total = jogador + computador
    print(f'você falor {jogador}')
