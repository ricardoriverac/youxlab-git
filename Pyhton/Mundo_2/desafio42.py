r1 = float(input('Digite um número: '))
r2 = float(input('Digite outro número: '))
r3 = float(input('Digite outro número: '))
if r1 == r2 == r3:
    print('Tipo de triângulo: Equilátero')
elif r1 == r2 or r2 == r3:
    print('Tipo de triângulo: Isósceles')
elif r1 != r2 != r3:
    print('Tipo de triângulo: Escaleno')