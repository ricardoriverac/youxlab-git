while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        print('Programa encerrado. Volte sempre!')
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 30)
