valores = []
pares = []
impar = []

for c in range (0, 8):
    valores.append(int(input('Digite valores: ')))
    print(valores)

for v in valores:
 if v % 2 == 0:
    pares.append(v)

 else:
    
    impar.append(v)
print(f'nos valores digitados {sorted(pares)} são pares e {sorted(impar)} são impar  ')