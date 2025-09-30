while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    for n in range(0,10):
        print(f'{numero} x {n} = {numero * n}')
print('programa encerrado! bye bye')