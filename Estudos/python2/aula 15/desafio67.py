multiplicação=0
count= 0
while count <= 10:
    Valor= int(input('Qual valor você deseja verificar?: '))
    if Valor <0:
        print('PROGRAMA ENCERRADO! ')
        break
    for count in range (1, 10):
        count=count+1
        multiplicação= Valor * count
        print(f'{Valor} x {count} = {multiplicação}')