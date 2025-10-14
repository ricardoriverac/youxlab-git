firstNumber = 0
secondNumber = 1
thirdNumber = 0
terms = int(input('Choose how many terms do you want'))
print (f'{firstNumber} > {secondNumber} > ', end='')
while terms > 2:
    thirdNumber = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = thirdNumber
    terms -= 1
    print (f'{thirdNumber}', end=' > ')
print ('End')