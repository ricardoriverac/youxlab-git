def readInt():
    while True:
        something = str(input('Enter a int number:\n->'))
        if something.isnumeric():
            print("It's a int number!")
            break
        else:
            print("It isn't a int number!")
readInt()