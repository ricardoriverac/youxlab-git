from time import sleep
def contagem(i, f, p):
    if p != abs(p):
        p = abs(p)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1)
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    else:
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.3)
        print('-----PRONTO!-----')


print('-=' * 15)
contagem(1, 10, 1)
print('-=' * 15)
contagem(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)