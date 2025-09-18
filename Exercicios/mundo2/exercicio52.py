#numero=int(input('Digite um numero: '))
#total=0

#for primo in range(1, numero):
   # if numero% primo==0:
     #   print

numero= int(input("Digite um numero: "))
total=0

for count in range(2,numero):
    if (numero % count == 0):
        print("Não é primo")
        total += 1

if(total==0):
    print("É primo")
