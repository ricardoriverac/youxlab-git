cm1 = int(input('digite um número: '))                               #tamanho 1 do diametro
cm2 = int(input('digite um outro número: '))                         #tamanho 2 do diametro
cm3 = int(input('digite um outro número: '))                         #tamanho 3 do diametro
soma1 = cm1 + cm2  
soma2 = cm2 + cm3
soma3 = cm3 + cm1
if cm1 <= soma2 and cm2 <= soma3 and cm3 <= soma1:
    print ('é possivel fazer um triângulo')
    if cm1 == cm2 and cm2 == cm3:
        print ('o triangulo é equilátero')
    elif cm1 == cm2 :
        print ('O triangulo é isóceles')
    elif cm2 == cm3 :
        print ('O triangulo é isóceles')
    elif cm3 == cm1 :
        print ('O triangulo é isóceles')
    else :
        print ('o triângulo é escaleno')
else:
    print ('não é possível fazer um triangulos com essas medidas')