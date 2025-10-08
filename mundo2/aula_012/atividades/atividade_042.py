'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escalano: todos os lados diferentes
'''

#Resultado

lado1 = int(input('Digite o 1° lado do triângulo: '))
lado2 = int(input('Digite o 2° lado do triângulo: '))
lado3 = int(input('Digite o 3° lado do triângulo: '))

if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print('E um triângulo ESCALENO!!')

elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1 :
    print('E um triângulo EQUILÁTERO!!')

else :
    print('E um triângulo ISÓSCELES!!')