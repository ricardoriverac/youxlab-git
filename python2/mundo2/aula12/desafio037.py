numero= int(input('Qual o número inteiro? '))
baseConversão= int(input('Qual modelo de conversão você quer?\n 1 para binário\n 2 para octal\n 3 para hexadecimal: '))
if baseConversão == (1):
    print('Sua conversão será binária!')
elif baseConversão == (2):
    print('Sua conversão será octal')
elif baseConversão == (3):
    print('Sua conversão será hexadecimal')
else:
    print('Escolha apenas uma das opções possíveis. ')