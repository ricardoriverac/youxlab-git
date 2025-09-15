number = int(input ('Enter a number'))
print ('''Choose the base of convergion:
[1] convert binary
[2] convert octal
[3] convert hexadecimal''')
option = int(input('Your option: '))
if option == 1:
    print(f'{number} converted into binary is equals to {bin(number)}')
elif option == 2:
    print(f'{number} converted into octal is equals to {oct(number)}')
elif option == 3:
    print(f'{number} converted into hexadecimal is equals to {hex(number)}')
else:
    print('Invalid option! Try again!!!')