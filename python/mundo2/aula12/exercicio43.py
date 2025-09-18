valor1=float(input('Primeiro segmento: '))
valor2=float(input('Segmento: '))
valor3=float(input('Terceiro segmento: '))
if valor1<valor2+valor3 and valor2<valor1+valor3 and valor3<valor1+valor2:
    print('Os segmentos acima PODEM FORMA um triângulo' , end='')
    if valor1==valor2==valor3:
        print('EQUILATERO!')
    elif valor1!=valor2!=valor3!=valor1:
        print('ESCALENO!')
else:
    print('Os segmentyos acima NAO PODEM FORMA triangulo')