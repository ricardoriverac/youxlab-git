'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaInt(numero):
    while True:
        numero2 = input(numero)
        if numero2.isnumeric():
            return numero2
        print('\033[31mERRO! Digite um número inteiro válido não conseguimos entender assim\033[m')


numero1 = leiaInt('Digite um número: ')
print(f'OBRIGADO, você acabou de digitar o número {numero1}')