firstNumber = int(input('Enter the first number'))
secondNumber = int(input('Enter the first number'))
thirdNumber = int(input('Enter the first'))
if firstNumber < secondNumber and firstNumber < thirdNumber:
    lowest = firstNumber
if secondNumber < firstNumber and secondNumber < thirdNumber:
    lowest = secondNumber
if thirdNumber < secondNumber and thirdNumber < firstNumber:
    lowest = thirdNumber
if firstNumber > secondNumber and firstNumber > thirdNumber:
    highest = firstNumber
if secondNumber > firstNumber and secondNumber > thirdNumber:
    highest = secondNumber
if thirdNumber > secondNumber and thirdNumber > firstNumber:
    highest = thirdNumber
print (f'The lowest number is {lowest} and the highest is {highest}')