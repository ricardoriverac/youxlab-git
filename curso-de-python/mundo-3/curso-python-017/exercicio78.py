listaNumeros = []
posMaior = 0
posMenor = 0

maior = 0
menor = 9999999

for c in range(5):
    numero = int(input(f'Digite  um valor para a posiçao {c}: '))
    listaNumeros.append(numero)

for i in range(len(listaNumeros)):
    n = listaNumeros[i]
    if n > maior:
         maior = n
         posMaior = i
    if n < menor:
         menor = n
         posMenor = i
print(f'maior {maior} na posisao {posMaior} \nmenor {menor} na posisao {posMenor} ')
    

   