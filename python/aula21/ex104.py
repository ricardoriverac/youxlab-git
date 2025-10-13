def leiaInt(numero):
    while True:
        numero2 = input(numero)
        if numero2.isnumeric():
            return numero2
        print('\033[31mERRO! Digite um número inteiro válido não conseguimos entender assim\033[m')


numero1 = leiaInt('Digite um número: ')
print(f'OBRIGADO, você acabou de digitar o número {numero1}')