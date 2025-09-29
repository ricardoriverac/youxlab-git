numero = int(input("digite um termo:"))
razao = int(input("digite uma razao:")) 
decimo = numero + (10 - 1) * razao 
for c in range(numero, 10, razao):
    print ('{}'.format(c), end=' ')
print('acabou')

