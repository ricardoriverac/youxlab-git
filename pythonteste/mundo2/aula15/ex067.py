while True:
    numero = int(input('Digite um número para ver sua tabuada[número negativo faz parar]: '))
    if numero < 0:
        break
    for contador in range(1, 11):
        print('{} x {:2} = {}'.format(numero, contador, numero * contador))
print('\033[31mPROGRAMA ENCERRADO\033[m')