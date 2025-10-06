reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))
if reta1 == reta2 == reta3:
    print('Os segmentos acima formam um TRIÂNGULO EQUILÁTERO!')
elif reta2 == reta1 or reta2 == reta3:
    print('Os segmentos acima formam um TRIÂNGULO ISÓSCELES!')
elif reta3 != reta1 != reta2:
    print('Os seguimentos acima formam um TRIÂNGULO ESCALENO!')