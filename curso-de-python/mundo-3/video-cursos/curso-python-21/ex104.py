def leiaInt(numeroInt):
    while True: 
        numeroInt = str(input('Digite um número inteiro: '))
        if numeroInt.isnumeric():
            return numeroInt

        else:
            print('ERRO! Digite um número inteiro válido!')

#Código Principal
numero = leiaInt('Digite um número inteiro: ')
print(numero)
print(f'Você digitou o número {numero}')