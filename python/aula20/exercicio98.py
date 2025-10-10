def contador(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    for c in range(a, b, c):
        print(c, end=' ')
    print('FIM!')
contador(1, 10, 1)
contador(10, -1, -2)
print('Agora é sua vez de personalizar a contagem!')
contador(a= int(input('Início: ')), b = int(input('Objetivo: ')), c = int(input('Parâmetro: ')))