finalList = []
primeiraLinha = [] 
segundaLinha = []
terceiraLinha = []
contador = 0
print ('Choose some numbers to fill a board (3 X 3)')
while contador != 3:
    numero = int(input('Digite um numero: '))
    primeiraLinha.append(numero)
    contador += 1
while contador != 6:
    numero = int(input('Digite um numero: '))
    segundaLinha.append(numero)
    contador += 1
while contador != 9:
    number = int(input('Digite um numero: '))
    terceiraLinha.append(number)
    contador += 1
finalList.append(primeiraLinha)
finalList.append(segundaLinha)
finalList.append(terceiraLinha)
print(f'[ {finalList[0][0]} ][ {finalList[0][1]} ][ {finalList[0][2]} ]')
print(f'[ {finalList[1][0]} ][ {finalList[1][1]} ][ {finalList[1][2]} ]')
print(f'[ {finalList[2][0]} ][ {finalList[2][1]} ][ {finalList[2][2]} ]')
