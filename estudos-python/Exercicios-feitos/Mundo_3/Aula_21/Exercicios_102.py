def factorial(number, show=False):
    factor = 1
    for count in range(number, 0, -1):
        if show:
            print(f'{number}', end='')
            number -= 1
            if count > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        factor *= count
    return factor
number = int(input('Enter a number:\n->'))
showInfo = str(input('Do you want to see the process?\nIf yes, enter [Y] or [y]\n->')).strip().upper()
if showInfo == 'Y':
    print(factorial(number, show=True))
else:
    print (factorial(number))