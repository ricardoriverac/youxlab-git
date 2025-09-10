reta1= float(input('Qual o valor da primeira reta? '))
reta2= float(input('Qual o valor da segunda reta?   '))
reta3= float(input('Qual o valor da terceira reta? '))
if reta1+reta2>reta3:
    print('O triangulo pode ser formado ')
elif reta1+reta3>reta2:
        print('O triangulo nao pode ser formado ')  
elif reta2+reta3>reta1:
        print('O triangulo nao pode ser formado')

#Verificação de equidade
if reta1 == reta2 and reta2== reta3:
       print('O triângulo é equilátero')
elif reta1 == reta3 or reta2 == reta1 or reta3== reta2:
       print('O triangulo é isósceles')
else:
       print('O triangulo é escaleno')