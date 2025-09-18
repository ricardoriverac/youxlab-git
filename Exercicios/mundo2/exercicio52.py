numero= int(input('Digite um numero: '))
total=0

for count in range(2,numero):
    if (numero % count == 0):
        print(f"O numero {numero} não é primo")
        total += 1

if(total==0):
    print(f"O numero {numero} é primo")
