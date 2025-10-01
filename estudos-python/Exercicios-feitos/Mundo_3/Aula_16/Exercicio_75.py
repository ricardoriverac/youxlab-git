numbers = ((int(input('Choose a number: '))),(int(input('Choose a number: '))),(int(input('Choose a number: '))),(int(input('Choose a number: '))))
evenNumber = 0
for individualNumber in numbers:
    if individualNumber % 2 == 0:
        evenNumber += 1
if 3 in numbers:
    numberThree = numbers.index(3)
    print (f'The 3 number is in the {numberThree+1}° position')
else:
    print ('There is no number 3')
numberNine = numbers.count(9)
print (f'There is {evenNumber} even numbers')
print (f'There is {numberNine} number 9')