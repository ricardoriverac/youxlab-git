import math
catetoAdjecente= int(input('Qual o valor do cateto Adjecente'))
catetoOposto=int(input('Qual o valor do cateto Oposto? '))
formula1= math.pow(catetoAdjecente, 2)
formula2=math.pow(catetoOposto, 2)
hipotenusa= math.sqrt(formula1+formula2)
seno= catetoOposto/hipotenusa
cosseno= catetoAdjecente/hipotenusa
tangente=catetoAdjecente/catetoOposto
print(catetoOposto)
print(catetoAdjecente)
print(f'O triângulo retângulo possui como valor da tangente {tangente}\n como valor do cosseno {cosseno}\n e como valor do seno {seno}')
