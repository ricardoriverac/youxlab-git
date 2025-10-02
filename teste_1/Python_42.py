primeiroSE = float(input('Primeiro segmento:'))
segundoSE = float(input('Segundo segmento:'))
terceiroSE = float(input('Terceiro segmento:'))
if primeiroSE < segundoSE + terceiroSE and segundoSE < primeiroSE + terceiroSE and terceiroSE < primeiroSE + segundoSE:
    print('O segmento acima pode SIM formar um triângulo:' ,end='')
    if primeiroSE == segundoSE == terceiroSE:
     print('EQUILÁTERO')
    
    elif primeiroSE != segundoSE != terceiroSE:
     print('ESCALENO')


elif print('O segmento acima pode SIM formar um triângulo:',end=''):
    print('ISÓSELES')
else:
 print('O segmento acima NÃO pode formar um triângulo')