def leiaint(string):
    while True:
        num = input(string)
        if num.isnumeric():
            return num
        else:
            print('ERRO! Digite um número inteiro válido.')
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

