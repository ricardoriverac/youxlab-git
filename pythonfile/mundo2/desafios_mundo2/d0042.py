reta1 = float(input('Digite o valor de uma reta '))
reta2 = float(input('Digite o valor da segunda reta'))
reta3 = float(input('Digite o valor da terceira reta'))
if reta1 == reta2 == reta3:
    print('As retas acima formam um triangulo eqilatero')
elif reta2 == reta1 or reta2 == reta3:
    print('As retas acima formam um trangulo isóceles')
elif reta3 != reta1 != reta2:
    print('As retas acima formam um triangulo escaleno')