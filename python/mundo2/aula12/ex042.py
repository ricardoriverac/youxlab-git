# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

reta1 =float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    if (reta1 == reta2) and (reta2 == reta3):
        print("O triângulo é EQUILÁTERO.")
    elif (reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3):
        print("O triângulo é ISÓSCELES.")
    else:
        print("O triângulo é ESCALENO.")
else:
    print("Os comprimentos ofernecidos não formam um triângulo.")