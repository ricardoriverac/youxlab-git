finalList = []
firstLine = [] 
seconLine = []
thirdLine = []
counter = 0
totalSum = 0
thirdLineSum = 0
highestSecondLine = 0
print ('Choose some numbers to fill a board (3 X 3)')
while counter != 3:
    number = int(input('Select some numbers: '))
    firstLine.append(number)
    counter += 1
    totalSum += number
while counter != 6:
    number = int(input('Select some numbers: '))
    seconLine.append(number)
    if counter == 6:
        highestSecondLine = number
    elif number > highestSecondLine:
        highestSecondLine = number
    totalSum += number
    counter += 1
while counter != 9:
    number = int(input('Select some numbers: '))
    thirdLine.append(number)
    counter += 1
    totalSum += number
    thirdLineSum += number
finalList.append(firstLine)
finalList.append(seconLine)
finalList.append(thirdLine)
print(f'[ {finalList[0][0]} ][ {finalList[0][1]} ][ {finalList[0][2]} ]')
print(f'[ {finalList[1][0]} ][ {finalList[1][1]} ][ {finalList[1][2]} ]')
print(f'[ {finalList[2][0]} ][ {finalList[2][1]} ][ {finalList[2][2]} ]')
print (f'The total sum is {totalSum}')
print (f'The sum of every number in third line is {thirdLineSum}')
print (f'The highest number in second line is {highestSecondLine}')