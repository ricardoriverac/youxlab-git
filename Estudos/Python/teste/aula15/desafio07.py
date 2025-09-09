reta1= float(input('Qual o valor da primeira reta? '))
reta2= float(input('Qual o valor da segunda reta?   '))
reta3= float(input('Qual o valor da terceira reta? '))
if reta1+reta2>reta3:
    if reta1+reta3>reta2:
        if reta2+reta3>reta1:
            print('O triangulo pode ser formado')
        else:
            print('O triangulo nao pode ser formado')
    else:
        print('O triangulo nao pode ser formado')
else:
    print('O triangulo nao pode ser formado')
