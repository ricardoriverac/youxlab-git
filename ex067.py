numero = int(input('Quer ver a tabuada de qual valor? '))
while numero >= 0:
    for c in range(1,11):
        resultado = c * numero
        print(f'{numero} X {c} = {resultado}')
    numero = int(input('Quer ver a tabuada de qual valor? '))