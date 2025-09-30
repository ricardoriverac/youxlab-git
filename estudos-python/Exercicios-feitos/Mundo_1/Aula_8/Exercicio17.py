#Calcula a hipotenusa em centímetros
import math
catetoOposto = int(input('Tamanho do cateto oposto'))
catetoAdjacente = int(input('Tamanho do cateto adjacente'))
quadradoDoCatetoOp = math.pow(catetoOposto,2)
quadradoDoCatetoAd = math.pow(catetoAdjacente,2)
somaDosCatetos = (quadradoDoCatetoAd + quadradoDoCatetoOp)
hipotenusa = math.sqrt(somaDosCatetos)
print (f'O tamanho em centímetros da hipotenusa é {hipotenusa:.2f}')