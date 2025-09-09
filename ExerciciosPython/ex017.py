from math import ceil, ceil
numOposto = float(input('Digite o número do cateto oposto: '))
numAdj = float(input('Digite o número do cateto adjacente: '))
hipotenusa = numOposto+numAdj
print('Se o cateto oposto é {} e o cateto adjacente é {} a hipotenusa é {}'.format(numOposto, numAdj, ceil(hipotenusa)))