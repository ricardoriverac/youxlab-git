while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-'*30)
    for contador in range (0, 11):
        print(f'{numero} x {contador} = {numero * contador}')
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE! ')