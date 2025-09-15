firstNumber = int(input('Enter a number: '))
secondNumber = int(input('Now choose another: '))
if firstNumber > secondNumber:
    print (f'The first number {firstNumber} is bigger than the second number {secondNumber}!')
elif secondNumber > firstNumber:
    print (f'The second number {secondNumber} is bigger than the first number {firstNumber}!')
elif firstNumber == secondNumber:
    print (f'The first number and the second number are both identical!')