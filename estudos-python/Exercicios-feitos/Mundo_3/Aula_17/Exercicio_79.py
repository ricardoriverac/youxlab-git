numbers = []
number = 0
option = ' '
while True:
    number = input('Enter some number:')
    numbers += number
    option = input('Do you want to continue? [N]No [Y]Yes').strip().upper()
    if option != 'Y':
        break
numbers.sort()
print(f'The choosen numbers is {numbers}!')