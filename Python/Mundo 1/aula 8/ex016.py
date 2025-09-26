from math import trunc, floor
num = float(input('Digite um número: ')) 
numeroInteiro = trunc (num)
print('O número {} tem a parte inteira {}'.format (num, floor (numeroInteiro)))