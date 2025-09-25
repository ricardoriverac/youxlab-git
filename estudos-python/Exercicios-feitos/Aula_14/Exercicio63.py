firstNumber = 0
originalFirstNumber = firstNumber
secondNumber = 1
originalSecondNumber = secondNumber
thirdNumber = 0
terms = int(input('Choose how many terms do you want'))
print (f'{originalFirstNumber} > {originalSecondNumber} > ', end='')
while terms > 1:
    thirdNumber = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = thirdNumber
    terms -= 1
    print (f'{thirdNumber}', end=' > ')
print ('End')