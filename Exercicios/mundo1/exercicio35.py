reta1=int(input('Digit o comprimento de uma reta: '))
reta2=int(input('Digite o compriment de outra reta: '))
reta3=int(input('Digite o comprimento de outra reta: '))

if reta1 + reta2>reta3:
    if reta1+reta3>reta2:
       reta2+reta3>reta1
    print('As retas formam um triangulo!')
else:
    if reta1+reta2<reta3:
      if reta1+reta3<reta2:
       reta2+reta3<reta1
    print('As retas nao formam um triangulo!')       
