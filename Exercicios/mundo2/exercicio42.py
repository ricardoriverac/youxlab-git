reta1=int(input('Digit o comprimento de uma reta: '))
reta2=int(input('Digite o compriment de outra reta: '))
reta3=int(input('Digite o comprimento de outra reta: '))

if reta1 + reta2>reta3:
    if reta1+reta3>reta2:
       reta2+reta3>reta1
    print('As retas formam um triangulo!')
    if reta1==reta2==reta3:
        print("Formam um triangulo equilátero.")
    elif reta1==reta2!=reta3:
            reta2==reta3!=reta1
            print("Formam um triangulo isósceles")
    elif reta1!=reta2!=reta3:
        print("Fomaram um trinagulo escaleno")

else:
    if reta1+reta2<reta3:
      if reta1+reta3<reta2:
       reta2+reta3<reta1
    print('As retas não formam um triangulo!')       
