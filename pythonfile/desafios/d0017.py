import math
cateto_oposto = float(input('Digite o valor do cateto oposto '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente'))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))