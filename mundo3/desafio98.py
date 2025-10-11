def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    for c in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(f'{c} ', end='')
    print('FIM\n')
contagem(1, 10, 1)
contagem(10, 0, 2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)