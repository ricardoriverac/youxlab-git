maiorpeso = 0
menorpeso = 0

for i in range(1,6):
    peso = float(input('Digite o peso da {} pessoa:'.format(i)))
    if i == 1:
        menorpeso = peso
        maiorpeso = peso

    if peso > maiorpeso:
        maiorpeso = peso
    
    if peso < menorpeso:
       menorpeso = peso

else:
    print('O maior peso lido foi de {}Kg'.format(maiorpeso))
    print('O menor peso lido foi de {}Kg'.format(menorpeso))
