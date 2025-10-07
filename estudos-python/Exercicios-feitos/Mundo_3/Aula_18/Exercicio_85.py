numbers = []
infoImpar = []
infoPar = []
for c in range(0,7):
    number = (int(input('Enter a number: ')))
    if number % 2 == 0:
        infoPar.append(number)
    elif number % 2 == 1:
        infoImpar.append(number)
infoPar.sort()
infoImpar.sort()
numbers.append(infoPar)
numbers.append(infoImpar)
print (f'Even numbers: {numbers[0]}')
print (f'Odd numbers: {numbers[1]}')