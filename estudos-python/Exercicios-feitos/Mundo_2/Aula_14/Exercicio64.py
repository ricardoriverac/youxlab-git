number = int(input('Choose a number to add: '))
some = 0
count = 0
while number != 999:
    some += number
    number = int(input('Choose another number to add: '))
    count +=1
print (f'The total some is {some}!')
print (f'{count} terms where needed to this!')