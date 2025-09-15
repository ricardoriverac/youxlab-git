reta1 = float(input('Digite o primeiro valor: '))
reta2 = float(input('Digite o segundo valor: '))
reta3 = float(input('Digite o terceiro valor: '))
# testando se é triangulo
if (reta1 + reta2) < reta3 and (reta2 + reta3) < reta1 and (reta3 + reta1)< reta2:
    print('Nao é um triangulo')
elif (reta1 == reta2) and (reta1 == reta3):
    print('Equilatero')
elif ( reta1 == reta2) and (reta2 == reta3) and (reta3 == reta1):
    print ('Isosceles')
else:
    print('Escaleno')



    