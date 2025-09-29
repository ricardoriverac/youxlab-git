lado = float(input(" comprimento do lado: "))
lado2 = float(input("comprimento do lado2: "))
lado3 = float(input("comprimento do lado3: "))
if lado == lado2 == lado3:
    print("voce consegue fazer um triangulo,ele sera um triangulo equilatero")
elif lado == lado2 > lado3:
    print("voce tem um triangulo isosceles")     
else:
    lado > lado2 > lado3 
    print("voce tem um triangulo escaleno")    
