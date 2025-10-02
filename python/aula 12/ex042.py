numero1 = float(input('Primeiro segmento: '))
numero2 = float(input('Segundo segmento: '))
numero3 = float(input('Terceiro segmento: '))
if numero1 < numero2 + numero3 and numero2 < numero1 + numero3 and numero3 < numero1 + numero2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if numero1 == numero2 == numero3:
        print('Equilátero')
    elif  numero1 != numero2 != numero3 != numero1:
        print('Escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos acima não podem formar triângulo')