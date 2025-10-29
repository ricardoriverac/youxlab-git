print('=== Analisador de Triângulos ===')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM formar um triângulo!')

    if r1 == r2 == r3:
        print('Tipo: EQUILÁTERO (todos os lados iguais)')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Tipo: ISÓSCELES (dois lados iguais)')
    else:
        print('Tipo: ESCALENO (todos os lados diferentes)')
else:
    print('As retas NÃO podem formar um triângulo.')
