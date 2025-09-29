while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} X {c} = {numero*c}')
print('Acabou!')
