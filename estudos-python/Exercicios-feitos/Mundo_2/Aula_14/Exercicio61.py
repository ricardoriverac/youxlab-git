firstOperator = int(input('Choose a number: '))
numberToBeAdded = int(input('Choose a multiplicator: '))
count = 1
while count != 10:
    print (firstOperator, end=' > ')
    firstOperator+=numberToBeAdded
    count += 1
print ('Fim')