numero = int(input('Quantos termos você quer mostrar: '))
primeiro = 0
segundo =1
cont = 0
while cont < numero:
    print(primeiro, end=' > ')
    primeiro,segundo = segundo,primeiro + segundo
    cont += 1
print('FIM')