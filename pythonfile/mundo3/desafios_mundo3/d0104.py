
def leiaint(msg):
    while True:

        num = input(msg)
        if num.isnumeric():
            return int(num)
        print('não é um valor inteiro')
    
numero = leiaint('Digite um valor: ')
print(f'Voce digitou o numero {numero}')
