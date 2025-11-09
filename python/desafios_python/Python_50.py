soma = 0 
cont = 0 
for c in range(1,7):
    numero = int(input('Digite um valor:'))
    if numero % 2 == 0:
     soma += numero
     cont  += 1 
#print('Você informou {} números e soma {}'.format(cont,soma))
print('Você informou {} números pares essa e a soma deles {}'.format(cont,soma))
