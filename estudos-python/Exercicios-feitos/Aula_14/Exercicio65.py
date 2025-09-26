count = 0
some = 0
highest = 0
lowest = 0
continueOrNot = str(input('DO YOU WANT TO CONTINUE? [N] No  [Y] Yes: ')).strip().upper()
firstContinue = continueOrNot
while continueOrNot == 'Y':
    number = int(input('Choose a number: '))
    count += 1
    if count == 1:
        highest = number
        lowest = number
    else:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    some += number
    average = some / count
    print ('DO YOU WANT TO CONTINUE?  [N] No [Y] Yes:')
    continueOrNot = str(input('')).strip().upper()
if firstContinue == 'Y':
    print (f'The average of all {count} choosen numbers is {average}!')
    print (f'The highest number was {highest}!')
    print (f'The lowest number was {lowest}!')
print('FIM DO PROGRAMA')