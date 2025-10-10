pares=list()
impares=list()
numeros=list()
count=0
for c in range (0, 8):
    count+=1
    numero=(int(input(f'Digite o {count}o valor: ')))
    numeros.append(numero)
    if numero % 2 ==0:
        pares.append(numeros[:])
    if numero % 2 == 1:
        impares.append(numeros[:])
    numeros.clear()
print(f'Os numeros pares digitados foram {pares}')
print(f'Os numeros ímpares digitados foram {impares}')
    
