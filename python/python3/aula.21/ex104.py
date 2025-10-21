def leiaint(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        print('ERRO!!!NAO É UM VALOR INTEIRO')
    
numero = leiaint('Digite um valor: ')
print(f'Voce digitou o numero {numero}')