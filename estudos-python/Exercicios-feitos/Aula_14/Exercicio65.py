number = int(input('Choose a number:\n>'))
count = 1
average = 0
some = 0
highest = number
lowest = number
print ('\nDO YOU WANT TO CONTINUE?\n')
continueOrNot = str(input('[N] No:\n[Y] Yes:\n\n')).strip().upper()
while continueOrNot == 'Y':
    number = int(input('\nChoose a number:\n\n>'))
    if number > highest:
        highest = number
    if number < lowest:
            lowest = number
    some += number
    average = some / count
    count += 1
    print ('\nDO YOU WANT TO CONTINUE?\n\n[N] No:\n[Y] Yes:\n')
    continueOrNot = str(input('')).strip().upper()
print (f'\nThe average of all {count} choosen numbers is {average}!')
print (f'\nThe highest number was {highest}!')
print (f'\nThe lowest number was {lowest}!')