num1 = int(input('escolha um número: '))        # número um
num2 = int(input('escolha outro número: '))     #número dois
if num1 > num2 :
    print ('O número {} é maoir que o número {}' .format(num1, num2))
elif num2 > num1 :
    print ('O número {} é maior que o número {}' .format(num2, num1))
elif num1 == num2 :
    print (' os dois numero tem o mesmo valor')