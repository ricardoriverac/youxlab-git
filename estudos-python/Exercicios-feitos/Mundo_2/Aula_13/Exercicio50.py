result = 0
for quantity in range(0,6):
    number = int(input('Enter 6 numbers: '))
    if number % 2 == 0:
        result += number
print (f'The result is {result}\nEND')