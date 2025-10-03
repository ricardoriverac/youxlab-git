numberList = []
counter = 0
option = 'Y'
while option == 'Y':
    number = int(input('Choose a number:'))
    numberList.append(number)
    counter += 1
    print (f'You choose the number {number}')
    option = input('Do you want to continue?:\nIf yes, enter [y] or [Y]').strip().upper()
print (f'There is {counter} inserted numbers')
if 5 in numberList:
    print ('There is the number 5')
numberList.sort(reverse=True)
print (numberList)