
valor=int(input('Que valor você quer sacar? R$'))
tot=valor
cedula=50
totalced=0
while True:
    if tot>=cedula:
        tot-=cedula
        totalced+=1
    else:
        if totalced>0:
            print(f'Total de {totalced} cedulas de R$ {cedula}')
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        if tot==0:
            break