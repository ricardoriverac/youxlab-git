normalList = []
evenList = []
oddList = []
option = 'Y'
count = 0
while option == 'Y':
    number = int(input('Choose a number: '))
    count += 1
    normalList.append(number)
    if number % 2 == 0:
        evenList.append(number)
    if number % 2 == 1:
        oddList.append(number)
    if count > 5:
        option = input('Do you want to continue?:\nIf yes, enter [y] or [Y]').strip().upper()
print (f'Every number list:{normalList}')
print (f'Even number list:{evenList}')
print (f'Odd number list:{oddList}')