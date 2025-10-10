
def leiaint(msg):
    while True:

        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        print('ERRO, Digite um valor inteiro.')
    
numero = leiaint('Digite um valor: ')
print(f'Voce digitou o numero {numero}')
