Termos= int(input('Quantos termos você quer ler em Fibonacci? '))
valoresTermos= Termos
count=1
fibonaci1= 0
fibonaci2=1
while count <= valoresTermos:
    fibonaci3=fibonaci1+fibonaci2
    print(f'{fibonaci3}>', end='')
    fibonaci1=fibonaci2
    fibonaci2=fibonaci3
    count+=1
print('FIM')