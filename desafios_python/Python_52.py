isPrimo = True 

numero = int(input('Digite um numero:'))
for c in range(2,numero):
    if (numero % c == 0):
        isPrimo = False 
        
if isPrimo == True:
    print('Ele e um número primo')
else: 
    print('Não e um número primo')