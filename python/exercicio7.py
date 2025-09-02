#algoritmo que lê um número e calcula seu dobro, triplo, quadrado e raiz quadrada

num1 = float(input('Digite qualquer número aq: '))
dobro = num1 * 2
triplo = num1 * 3
quad = num1**2
raiz = num1**(1/2)
print('O dobro, triplo, quadrado e raiz quadrada do número {0} são, respectivamente, os valores: \nDobro: {1}; \nTriplo: {2} \nQuadrado: {3} \nRaiz: {4}'.format(num1, dobro, triplo, quad, raiz))