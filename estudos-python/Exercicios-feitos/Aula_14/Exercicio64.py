number = int(input('Choose a number to add: '))
some = 0
while number != 999:
    some += number
    number = int(input('Choose another number to add: '))
print (f'The total some is {some}!')