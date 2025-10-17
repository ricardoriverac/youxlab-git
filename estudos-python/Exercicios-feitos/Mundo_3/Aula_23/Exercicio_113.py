def readInt(message):
    while True:
        try:
            intNumber = input(message)
            intNumber = int(intNumber)
        except:
            print('\nERROR: Somethin went REALLY wrong!\n')
        else:
            print('You get it!')
            return intNumber

def readFloat(message2):
    while True:
        try:
            floatNumber = input(message2)
            floatNumber = float(floatNumber)
        except:
            print('\nERROR: Somethin went REALLY wrong!\n')
        else:
            print('Yes it is a float number!')
            return floatNumber

tentativa1 = readInt('Enter a integer number\n->')
tentativa2 = readFloat('Enter a floating point number\n->')

print(f'The inserted integer number is {tentativa1}')
print(f'The inserted floating point number is {tentativa2}')