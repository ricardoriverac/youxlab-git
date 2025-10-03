numbers = [int(input('Choose a number: ')),int(input('Choose a number: ')),int(input('Choose a number: ')),int(input('Choose a number: ')),int(input('Choose a number: '))]
highestNumber = 0
lowestNumber = 0
highestPosition = 0
lowestPosition = 0
for position, individualNumber in enumerate(numbers):
    if position == 0:
        highestNumber = individualNumber
        lowestNumber = individualNumber
        highestPosition = position
        lowestPosition = position
    else:
        if individualNumber > highestNumber:
            highestNumber = individualNumber
            highestPosition = position
        if individualNumber < lowestNumber:
            lowestNumber = individualNumber
            lowestPosition = position
numbers.sort()
print (f'The highest number is {highestNumber} in the {highestPosition+1}°position and the lowest number is {lowestNumber} in the {lowestPosition+1}°position!')