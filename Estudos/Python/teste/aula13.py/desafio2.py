import math
catetoOposto= float(input('Qual o valor do cateto oposto do triângulo retângulo? [º] '))
catetoAdjacente= float(input('Qual o valor do cateto adjacente do triângulo retângulo? [º] '))
formula1= float(math.pow(catetoAdjacente, 2))
formula2= float(math.pow(catetoOposto, 2))
hipotenusa= math.sqrt(formula1+formula2)
print(catetoAdjacente)
print(catetoOposto)
print(f'O valor da hipotenusa do triângulo retângulo é {hipotenusa}')
