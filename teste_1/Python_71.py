print('=' * 30)
print('BANCO CEV')
print('=' * 30)
valor = float(input('Que valor você quer sacar?R$:'))
total = valor 
cedulas = 50 
totalcedulas = 0 

while True:
    if total >=cedulas:
        total -= cedulas
        totalcedulas += 1
    else:
        print(f'Total de {totalcedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalcedulas = 0 
        if totalcedulas == 0:
            break