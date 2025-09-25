firstOperator = int(input('Choose a number: '))
numberToBeAdded = int(input('Choose a number to add in sequence: '))
count = 1
while count != 11:
    print (firstOperator, end=' > ')
    firstOperator+=numberToBeAdded
    count += 1
print ('End')
newTerms = int(input('How much do you want to see more terms?: '))
if newTerms > 0:
    while count != 11+newTerms:
        print (firstOperator, end=' > ')
        firstOperator+=numberToBeAdded
        count += 1
print ('End')