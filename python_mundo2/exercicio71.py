quantidade = 0
valor = int(input('quanto você quer sacar? '))
while True: 
    if valor >= 50 :
        valor = valor - 50 
        quantidade = quantidade + 1
    if valor < 50:
        break
while True:
    if valor >= 20 :
        valor = valor - 20 
        quantidade = quantidade + 1
    if valor < 20:
        break
while True:
    if valor >= 10:
        valor = valor - 10 
        quantidade = quantidade + 1
    if valor < 10:
        break
while True:
    if valor >= 1:
        valor = valor - 1
        quantidade += 1
    if valor < 1:
        break
print ('você ter q sacar {} notas' .format (quantidade))